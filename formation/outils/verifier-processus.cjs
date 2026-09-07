// @spec formation/SPECIFICATION.md#verification
const assert=require('node:assert/strict');
const {spawn}=require('node:child_process');
const {once}=require('node:events');
const {stopChild}=require('./processus.cjs');
async function main(){
  const ended=spawn(process.execPath,['-e','process.exit(0)']);
  await once(ended,'exit');
  assert.equal((await stopChild(ended)).already_stopped,true);
  const signalled=spawn(process.execPath,['-e','process.kill(process.pid,"SIGTERM")']);
  await once(signalled,'exit');
  assert.equal((await stopChild(signalled)).already_stopped,true);
  const stubborn=spawn(process.execPath,['-e','process.on("SIGINT",()=>{});process.on("SIGTERM",()=>{});setInterval(()=>{},1000);console.log("ready");']);
  await once(stubborn.stdout,'data');
  const result=await stopChild(stubborn,{graceMs:100});
  assert.equal(result.requested_signal,'SIGKILL');
  assert.equal(result.forced,true);
  console.log('3 cas d’arrêt réussis : sortie, signal antérieur, enfant ignorant SIGINT/SIGTERM.');
}
main().catch(error=>{console.error(error);process.exitCode=1;});
