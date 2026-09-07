// @spec formation/SPECIFICATION.md#edition | formation/SPECIFICATION.md#verification
// PDF, PowerPoint éditable, captures et contrôles navigateur des supports.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');
const PptxGenJS = require('pptxgenjs');
const {createHash}=require('node:crypto');
const root = path.resolve(__dirname, '..');
const out = path.join(root, 'exports');
const captures = path.join(out, 'captures');
const pngDir = path.join(out, 'figures');
fs.mkdirSync(captures, {recursive:true});
fs.mkdirSync(pngDir, {recursive:true});
const slides = JSON.parse(fs.readFileSync(path.join(root, 'slides.json'), 'utf8'));
const figures = JSON.parse(fs.readFileSync(path.join(root, 'illustrations.json'), 'utf8'));
const browserPath = process.env.FORMATION_CHROMIUM;
const report = {slides:slides.length, checks:[], overflow:[], external_requests:[]};
const sourceNames=['programme.json','slides.json','illustrations.json','styles.css','lecteur-slides.js','outils/construire.py','outils/exporter.cjs','SYLLABUS.md','INSTALLATION.md','EXERCICES.md','EVALUATION.md','CORRIGES.md','CORRIGE_FINAL.md','FICHES.md','GLOSSAIRE.md','SOURCES.md','ANIMATION.md',...fs.readdirSync(path.join(root,'cours')).filter(n=>n.endsWith('.md')).map(n=>'cours/'+n)];
report.sources=Object.fromEntries(sourceNames.map(n=>[n,createHash('sha256').update(fs.readFileSync(path.join(root,n))).digest('hex')]));
function check(name, ok, details) {
  report.checks.push({name, ok, details});
  if (!ok) throw new Error(name + ': ' + JSON.stringify(details));
}

async function main() {
  const browser = await chromium.launch({headless:true, ...(browserPath?{executablePath:browserPath}:{})});
  try {
    report.browser = await browser.version();
    const page = await browser.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:1});
    page.on('request', request => {if (/^https?:/.test(request.url())) report.external_requests.push(request.url());});
    for (const name of ['cours','cahier-exercices','corriges','guide-animation']) {
      await page.goto(pathToFileURL(path.join(out,name+'.html')).href);
      await page.evaluate(()=>document.fonts.ready);
      check(name+' images chargées', await page.locator('img').evaluateAll(imgs=>imgs.every(i=>i.complete && i.naturalWidth>0)));
      const badLinks = await page.locator('a[href^="#"]').evaluateAll(links=>links.filter(a=>!document.getElementById(decodeURIComponent(a.hash.slice(1)))).map(a=>a.hash));
      check(name+' ancres internes',badLinks.length===0,badLinks);
      await page.pdf({path:path.join(out,name+'.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true,tagged:true,outline:true,displayHeaderFooter:true,headerTemplate:'<span></span>',footerTemplate:'<div style="font:9px Arial;width:100%;text-align:center;color:#4B5563">P2Enjoy · Codage agentique · <span class="pageNumber"></span> / <span class="totalPages"></span></div>'});
      if(name==='cours') {
        await page.screenshot({path:path.join(captures,'cours-bureau.png')});
        await page.setViewportSize({width:390,height:844});
        const horizontal=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,viewport:innerWidth}));
        check('cours mobile sans débordement horizontal',horizontal.scroll<=horizontal.viewport,horizontal);
        await page.screenshot({path:path.join(captures,'cours-mobile.png')});
        await page.setViewportSize({width:1440,height:1000});
      }
      console.log('PDF : '+name);
    }
    await page.setViewportSize({width:1280,height:820});
    for(const [fragment,expected] of [['1.5',1],['abc',1],['0',1],['999',80]]){
      await page.goto(pathToFileURL(path.join(out,'slides.html')).href+'#'+fragment);
      await page.reload();
      check('fragment de navigation #'+fragment,await page.locator('#position').innerText()===`Diapositive ${expected} sur 80`);
    }
    await page.goto(pathToFileURL(path.join(out,'slides.html')).href);
    await page.reload();
    check('80 slides HTML',await page.locator('.slide').count()===80);
    await page.keyboard.press('ArrowRight');
    check('flèche suivante',await page.locator('#position').innerText()==='Diapositive 2 sur 80');
    await page.locator('#toggle-notes').click();
    check('notes accessibles',await page.locator('#notes').isVisible() && await page.locator('#toggle-notes').getAttribute('aria-expanded')==='true');
    await page.keyboard.press('n');
    check('raccourci notes',!await page.locator('#notes').isVisible());
    await page.keyboard.press('End');
    check('dernière slide',await page.locator('#position').innerText()==='Diapositive 80 sur 80');
    await page.keyboard.press('Home');
    check('première slide',await page.locator('#previous').isDisabled());
    const shots = new Set([1,3,4,8,18,29,43,49,54,59,64,69,74,78,80]);
    for(let i=0;i<slides.length;i++) {
      const geometry=await page.locator('.slide.active').evaluate(el=>{
        const bounds=el.getBoundingClientRect();
        const takeaway=el.querySelector('.takeaway').getBoundingClientRect();
        const elements=[...el.children].filter(e=>!['TEMPLATE','FOOTER'].includes(e.tagName)&&!e.classList.contains('takeaway'));
        const problems=[];
        for(const e of elements) {
          const r=e.getBoundingClientRect();
          if(r.right>bounds.right-30 || r.left<bounds.left || r.bottom>takeaway.top-8) problems.push({tag:e.tagName,class:e.className,top:r.top-bounds.top,bottom:r.bottom-bounds.top,takeaway:takeaway.top-bounds.top});
          if(e.scrollWidth>e.clientWidth+1) problems.push({tag:e.tagName,reason:'horizontal'});
          const style=getComputedStyle(e);
          if(style.maxHeight!=='none'&&e.scrollHeight>e.clientHeight+1) problems.push({tag:e.tagName,reason:'vertical interne plafonné'});
        }
        const footer=el.querySelector('footer').getBoundingClientRect();
        if(takeaway.bottom>footer.top-8||footer.bottom>bounds.bottom||footer.right>bounds.right)problems.push({reason:'conclusion/pied de page'});
        return problems;
      });
      if(geometry.length) report.overflow.push({slide:i+1,geometry});
      if(shots.has(i+1)) await page.locator('.slide.active').screenshot({path:path.join(captures,`slide-${String(i+1).padStart(2,'0')}.png`)});
      if(i<slides.length-1) await page.locator('#next').click();
    }
    await page.pdf({path:path.join(out,'slides.pdf'),printBackground:true,preferCSSPageSize:true,tagged:true});
    await page.setViewportSize({width:390,height:844});
    await page.keyboard.press('Home');
    check('slides mobile sans débordement',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
    await page.screenshot({path:path.join(captures,'slides-mobile.png')});
    for(const fig of figures) {
      await page.goto(pathToFileURL(path.join(root,'illustrations',fig.id+'.svg')).href);
      await page.setViewportSize({width:1200,height:300});
      await page.locator('svg').evaluate(svg=>{svg.setAttribute('viewBox','0 80 1200 300');svg.setAttribute('height','300');});
      await page.screenshot({path:path.join(pngDir,fig.id+'.png')});
    }
    check('aucune ressource distante au rendu',report.external_requests.length===0,report.external_requests);
    fs.writeFileSync(path.join(out,'controle-rendu.json'),JSON.stringify(report,null,2));
    check('aucun chevauchement détecté sur les slides',report.overflow.length===0,report.overflow);
    await powerpoint();
  } finally {
    await browser.close();
    fs.writeFileSync(path.join(out,'controle-rendu.json'),JSON.stringify(report,null,2));
  }
}

async function powerpoint() {
  const pptx = new PptxGenJS();
  pptx.layout='LAYOUT_WIDE';
  pptx.author='P2Enjoy';
  pptx.subject='Formation autonome et animation premium — syllabus';
  pptx.title='Coder avec un agent : les bases, la méthode, puis l’usine';
  pptx.company='P2Enjoy';
  pptx.lang='fr-FR';
  pptx.theme={headFontFace:'Arial',bodyFontFace:'Arial',lang:'fr-FR'};
  const brand='23468C',ink='0D0D0D',muted='4B5563',accent='D9CF4A';
  for(const [index,s] of slides.entries()) {
    const slide=pptx.addSlide();
    const hero=s.type==='hero';
    const color=hero?'FFFFFF':ink;
    slide.background={color:hero?brand:'FFFFFF'};
    const label=s.module===0?'PARCOURS':s.module===16?'ÉVALUATION FINALE':`MODULE ${String(s.module).padStart(2,'0')} / 15`;
    slide.addText(label,{x:.67,y:.48,w:11.9,h:.3,fontSize:13,bold:true,color:hero?'FFFFFF':brand,margin:0,charSpacing:2});
    slide.addText(s.title,{x:.67,y:hero?1.08:.95,w:12,h:hero?1.45:1.05,fontSize:hero?40:32,bold:true,color,margin:0,breakLine:false,valign:'mid'});
    let y=hero?2.75:2.17;
    if(s.lead) {
      slide.addText(s.lead,{x:.67,y,w:11.85,h:.92,fontSize:22,color,margin:0,valign:'top',breakLine:false});
      y+=1.12;
    }
    if(s.points) {
      for(const point of s.points) {
        slide.addShape(pptx.ShapeType.rect,{x:.72,y:y+.12,w:.07,h:.07,line:{color:hero?accent:brand},fill:{color:hero?accent:brand}});
        slide.addText(point,{x:.97,y,w:11.4,h:.73,fontSize:21,color,margin:0,valign:'top',breakLine:false});
        y+=.81;
      }
    }
    if(s.case) {
      slide.addShape(pptx.ShapeType.rect,{x:.67,y:2.23,w:12,h:3.05,line:{color:'F7F8FA'},fill:{color:'F7F8FA'}});
      slide.addShape(pptx.ShapeType.rect,{x:.67,y:2.23,w:.07,h:3.05,line:{color:brand},fill:{color:brand}});
      slide.addText(s.case,{x:.97,y:2.48,w:11.35,h:2.6,fontFace:'Courier New',fontSize:21,color:ink,margin:0,valign:'top',paraSpaceAfter:8,breakLine:false});
    }
    if(s.figure){const f=figures.find(f=>f.id===s.figure);slide.addImage({path:path.join(pngDir,s.figure+'.png'),x:.67,y:2.38,w:12,h:3,altText:f.title+'. '+f.subtitle+' '+f.nodes.map(n=>n.join(' : ')).join('; ')+'. '+f.footer});}
    slide.addShape(pptx.ShapeType.line,{x:.67,y:6.35,w:12,h:0,line:{color:accent,width:2}});
    slide.addText(s.takeaway,{x:.67,y:6.48,w:12,h:.55,fontSize:15,bold:true,color,margin:0,valign:'top'});
    slide.addText('P2Enjoy · Les bases, la méthode, puis l’usine',{x:.67,y:7.16,w:10,h:.15,fontSize:9,color:hero?'FFFFFF':muted,margin:0});
    slide.addText(`${index+1} / ${slides.length}`,{x:11.7,y:7.13,w:.95,h:.2,fontSize:9,color:hero?'FFFFFF':muted,align:'right',margin:0});
    slide.addNotes(Object.entries(s.notes).map(([k,v])=>k.toUpperCase()+'\n'+v).join('\n\n'));
  }
  await pptx.writeFile({fileName:path.join(out,'slides.pptx'),compression:true});
  console.log('PowerPoint : '+slides.length+' slides avec notes et texte éditable.');
}
main().catch(error=>{console.error(error);process.exitCode=1;});
