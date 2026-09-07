// @spec formation/SPECIFICATION.md#verification
// Arrêter uniquement un enfant déjà créé par le contrôleur, avec attente bornée.
async function stopChild(child,{graceMs=1500}={}) {
  const terminal=()=>child.exitCode!==null||child.signalCode!==null;
  if(terminal())return {already_stopped:true,code:child.exitCode,signal:child.signalCode};
  if(!child.pid)throw new Error('Enfant sans identifiant de processus : arrêt impossible à qualifier.');
  let onExit;
  const exited=new Promise(resolve=>{onExit=(code,signal)=>resolve({code,signal});child.once('exit',onExit);});
  try{
    for(const signal of ['SIGINT','SIGTERM','SIGKILL']){
      if(terminal())return {code:child.exitCode,signal:child.signalCode};
      child.kill(signal);
      let timer;
      const result=await Promise.race([exited,new Promise(resolve=>{timer=setTimeout(()=>resolve(null),graceMs);})]);
      clearTimeout(timer);
      if(result)return {...result,requested_signal:signal,forced:signal!=='SIGINT'};
    }
    throw new Error('Enfant non arrêté après trois délais bornés ; intervention nécessaire.');
  }finally{child.removeListener('exit',onExit);}
}
module.exports={stopChild};
