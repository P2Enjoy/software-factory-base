// @spec formation/SPECIFICATION.md#atelier | formation/SPECIFICATION.md#verification
// Preuves rejouables sur trois copies neuves et des serveurs 127.0.0.1 uniquement.
const fs=require('node:fs');
const os=require('node:os');
const path=require('node:path');
const {spawn,spawnSync}=require('node:child_process');
const {chromium}=require('playwright');
const {stopChild}=require('./processus.cjs');
const {createHash}=require('node:crypto');
const root=path.resolve(__dirname,'..');
const out=path.join(root,'exports');
const captures=path.join(out,'captures');
fs.mkdirSync(captures,{recursive:true});
const temp=fs.mkdtempSync(path.join(os.tmpdir(),'formation-preuves-'));
const python=process.env.FORMATION_PYTHON || 'python3';
const report={executed_at:new Date().toISOString(),platform:process.platform,temp,checks:[],tests:{},servers:[]};
const sourceNames=['outils/verifier-atelier.cjs','outils/processus.cjs',...fs.readdirSync(path.join(root,'atelier'),{recursive:true}).filter(n=>!n.includes('__pycache__')&&fs.statSync(path.join(root,'atelier',n)).isFile()).map(n=>'atelier/'+n.replaceAll(path.sep,'/'))];
report.sources=Object.fromEntries(sourceNames.map(n=>[n,createHash('sha256').update(fs.readFileSync(path.join(root,n))).digest('hex')]));
const running=new Set();
function check(name,ok,details){report.checks.push({name,ok,details});if(!ok)throw new Error(name+': '+JSON.stringify(details));}
function command(args,cwd){return spawnSync(python,args,{cwd,encoding:'utf8',timeout:60000});}
async function start(version){
  const child=spawn(python,['app.py','--port','0','--db','preuve.sqlite3'],{cwd:path.join(temp,version),stdio:['ignore','pipe','pipe']});
  running.add(child);
  const url=await new Promise((resolve,reject)=>{
    let output='';const timer=setTimeout(()=>reject(new Error('Serveur non démarré')),8000);
    child.once('error',error=>{clearTimeout(timer);reject(error);});
    child.once('exit',code=>{clearTimeout(timer);reject(new Error('Serveur arrêté avant écoute : '+code));});
    child.stdout.on('data',chunk=>{output+=chunk;const match=output.match(/http:\/\/127\.0\.0\.1:\d+/);if(match){clearTimeout(timer);resolve(match[0]);}});
  });
  report.servers.push({version,url});
  return {child,url};
}
async function stop(server){
  const result=await stopChild(server.child);
  if(!report.stops)report.stops=[];
  report.stops.push(result);
  running.delete(server.child);
}
async function login(page,url,profile){await page.goto(url+'/');await page.getByLabel('Profil',{exact:true}).selectOption(profile);await page.getByRole('button',{name:'Entrer',exact:true}).click();}
async function rows(page,url){const response=await page.context().request.get(url+'/api/demandes');check('lecture API autorisée',response.status()===200);return response.json();}

async function main(){
  report.python=command(['--version'],root).stdout.trim();
  for(const version of ['depart','reference','finale']){
    const created=command([path.join(root,'atelier','preparer.py'),path.join(temp,version),'--version',version],root);
    check('préparer '+version,created.status===0,created.stderr);
    const result=command(['-m','unittest','-v'],path.join(temp,version));
    const output=result.stdout+result.stderr;
    report.tests[version]={exit_code:result.status,output};
    if(version==='depart'){
      check('départ : sept tests dont exactement quatre échecs attendus',result.status===1 && /Ran 7 tests/.test(output) && /FAILED \(failures=4\)/.test(output) && !/^ERROR:/m.test(output));
      for(const test of ['test_title_bounds_and_normalization','test_role_and_ownership_matrix','test_invalid_title_is_refused_without_creation','test_foreign_request_refused_without_mutation'])check('rouge pédagogique '+test,new RegExp('FAIL: '+test).test(output));
    }else check(version+' : suite complète verte',result.status===0 && output.includes('Ran '+(version==='finale'?12:7)+' tests') && /\nOK\s*$/.test(output));
    const repeated=command([path.join(root,'atelier','preparer.py'),path.join(temp,version),'--version',version],root);
    check('refus de remplacer '+version,repeated.status!==0 && repeated.stderr.includes('destination existe déjà'));
  }
  const browser=await chromium.launch({headless:true,...(process.env.FORMATION_CHROMIUM?{executablePath:process.env.FORMATION_CHROMIUM}:{})});
  try{
    report.browser=await browser.version();
    const page=await browser.newPage({viewport:{width:1280,height:900}});
    let server=await start('reference');
    await login(page,server.url,'bob');
    check('accueil Bob : trois demandes',await page.locator('article').count()===3);
    await page.getByRole('link',{name:'Nouvelle demande',exact:true}).click();
    await page.getByLabel('Titre de la demande',{exact:true}).fill('   ');
    await page.getByRole('button',{name:'Créer la demande',exact:true}).click();
    check('refus de validation visible',await page.getByRole('alert').isVisible());
    check('saisie invalide conservée',await page.getByLabel('Titre de la demande',{exact:true}).inputValue()==='   ');
    check('aucune insertion après refus',(await rows(page,server.url)).length===3);
    await page.screenshot({path:path.join(captures,'atelier-refus.png')});
    await page.getByLabel('Titre de la demande',{exact:true}).fill('Installer le réseau');
    await page.getByRole('button',{name:'Créer la demande',exact:true}).click();
    check('création visible depuis le formulaire',await page.getByRole('heading',{name:'Installer le réseau',exact:true}).isVisible());
    const created=(await rows(page,server.url)).at(-1);
    check('propriétaire et statut persistés',created.owner==='bob'&&created.status==='ouvert');
    await page.reload();
    check('création retrouvée après rechargement',await page.locator('article').count()===4);
    await page.getByRole('button',{name:'Clore la demande 2',exact:true}).click();
    check('clôture de sa demande visible',(await page.getByRole('article',{name:'Demande 2',exact:true}).innerText()).includes('Fermée'));
    check('Bob : clôture tierce non proposée',await page.getByRole('button',{name:'Clore la demande 1',exact:true}).count()===0);
    const denied=await page.context().request.post(server.url+'/api/demandes/1/fermer',{data:{}});
    check('appel direct Bob refusé sans mutation',denied.status()===403&&(await rows(page,server.url))[0].status==='ouvert');
    await page.screenshot({path:path.join(captures,'atelier-liste.png')});
    await stop(server);
    server=await start('reference');
    await page.goto(server.url+'/demandes');
    check('session éphémère après redémarrage',await page.getByRole('heading',{name:'Accès refusé',exact:true}).count()===1 || (await page.locator('main').innerText()).includes('Choisissez un profil'));
    await login(page,server.url,'bob');
    const restored=await rows(page,server.url);
    check('données conservées, seed non réappliqué',restored.length===4 && restored.at(-1).title==='Installer le réseau' && restored[1].status==='ferme');
    await page.getByRole('link',{name:'Nouvelle demande',exact:true}).click();
    await page.getByLabel('Titre de la demande',{exact:true}).fill('W'.repeat(80));
    await page.getByRole('button',{name:'Créer la demande',exact:true}).click();
    await page.setViewportSize({width:390,height:844});
    check('liste mobile sans débordement, titre long',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.screenshot({path:path.join(captures,'atelier-mobile.png'),fullPage:true});
    await login(page,server.url,'alice');
    check('cible de clôture tierce : demande 4 ouverte de Bob',(await rows(page,server.url)).some(r=>r.id===4&&r.owner==='bob'&&r.status==='ouvert'));
    await page.getByRole('button',{name:'Clore la demande 4',exact:true}).click();
    check('Alice peut clore autrui',(await rows(page,server.url)).find(r=>r.id===4).status==='ferme');
    await login(page,server.url,'eve');
    check('Eve : lecture sans commande d’écriture',await page.locator('article').count()===5 && await page.getByRole('link',{name:'Nouvelle demande',exact:true}).count()===0 && await page.getByRole('button',{name:/Clore/}).count()===0);
    await page.goto(server.url+'/');
    await page.keyboard.press('Tab');
    const focus=await page.evaluate(()=>{const s=getComputedStyle(document.activeElement);return {text:document.activeElement.textContent,outline:s.outlineStyle,width:parseFloat(s.outlineWidth),color:s.outlineColor};});
    check('indicateur de focus déclaré et non transparent',focus.outline!=='none'&&focus.width>=2&&!['transparent','rgba(0, 0, 0, 0)'].includes(focus.color),focus);
    await page.screenshot({path:path.join(captures,'atelier-clavier.png')});
    await stop(server);
    server=await start('finale');
    await page.setViewportSize({width:1280,height:900});
    await login(page,server.url,'alice');
    const before=(await rows(page,server.url))[2];
    await page.getByRole('button',{name:'Rouvrir la demande 3',exact:true}).click();
    const reopened=(await rows(page,server.url))[2];
    check('réouverture par parcours réel',reopened.status==='ouvert' && reopened.id===before.id && reopened.title===before.title && reopened.owner===before.owner);
    check('clôture disponible après réouverture',await page.getByRole('button',{name:'Clore la demande 3',exact:true}).isVisible());
    await page.screenshot({path:path.join(captures,'atelier-finale.png')});
    await page.getByRole('button',{name:'Clore la demande 3',exact:true}).click();
    for(const profile of ['bob','eve']){
      await login(page,server.url,profile);
      check(profile+' : aucune réouverture affichée',await page.getByRole('button',{name:/Rouvrir/}).count()===0);
      const response=await page.context().request.post(server.url+'/api/demandes/3/rouvrir',{data:{}});
      check(profile+' : réouverture API refusée sans mutation',response.status()===403 && (await rows(page,server.url))[2].status==='ferme');
    }
    await page.setViewportSize({width:390,height:844});
    await login(page,server.url,'alice');
    let reached=false;
    for(let tab=0;tab<20;tab++){
      await page.keyboard.press('Tab');
      reached=await page.getByRole('button',{name:'Rouvrir la demande 3',exact:true}).evaluate(button=>button===document.activeElement);
      if(reached)break;
    }
    check('réouverture atteinte par Tab sans focus programmatique',reached);
    const keyboardNavigation=page.waitForEvent('framenavigated',{predicate:frame=>frame===page.mainFrame()});
    await page.keyboard.press('Enter');
    await keyboardNavigation;
    await page.waitForLoadState('load');
    check('réouverture au clavier à petite largeur',(await rows(page,server.url))[2].status==='ouvert' && await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.screenshot({path:path.join(captures,'atelier-finale-mobile.png'),fullPage:true});
    await stop(server);
  }finally{await browser.close();}
  console.log(JSON.stringify({temp,checks:report.checks.length,failed:report.checks.filter(c=>!c.ok).length,tests:{depart:'7 tests, 4 échecs attendus',reference:'7 réussites',finale:'12 réussites'}},null,2));
}
main().catch(error=>{report.error=String(error);console.error(error);process.exitCode=1;}).finally(async()=>{
  try{for(const child of [...running]){try{await stop({child});}catch(error){report.cleanup_error=String(error);process.exitCode=1;}}}
  finally{fs.writeFileSync(path.join(out,'controle-atelier.json'),JSON.stringify(report,null,2));}
});
