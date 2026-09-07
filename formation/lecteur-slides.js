// @spec formation/SPECIFICATION.md#slides | docs/DESIGN_SYSTEM_APP.md#composition
(() => {
  const slides=[...document.querySelectorAll('.slide')], stage=document.querySelector('.deck-stage');
  const notes=document.querySelector('.notes'), toggle=document.querySelector('#toggle-notes');
  const requested=Number(location.hash.slice(1)||1);
  let current=Number.isInteger(requested)?Math.max(0,Math.min(slides.length-1,requested-1)):0;
  const fit=()=>{const scale=Math.min(1,stage.clientWidth/1280);slides[current].style.transform=`scale(${scale})`;stage.style.height=`${720*scale}px`;};
  function show(index){current=Math.max(0,Math.min(slides.length-1,index));slides.forEach((s,i)=>{s.classList.toggle('active',i===current);s.setAttribute('aria-hidden',String(i!==current));});document.querySelector('#position').textContent=`Diapositive ${current+1} sur ${slides.length}`;document.querySelector('#previous').disabled=current===0;document.querySelector('#next').disabled=current===slides.length-1;notes.innerHTML=slides[current].querySelector('template').innerHTML;history.replaceState(null,'',`#${current+1}`);fit();}
  document.querySelector('#previous').addEventListener('click',()=>show(current-1));
  document.querySelector('#next').addEventListener('click',()=>show(current+1));
  toggle.addEventListener('click',()=>{notes.hidden=!notes.hidden;toggle.setAttribute('aria-expanded',String(!notes.hidden));});
  document.addEventListener('keydown',e=>{if(e.altKey||e.ctrlKey||e.metaKey||/INPUT|TEXTAREA|SELECT/.test(e.target.tagName))return;if(e.key==='ArrowRight'||e.key==='PageDown'){e.preventDefault();show(current+1);}if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();show(current-1);}if(e.key==='Home'){e.preventDefault();show(0);}if(e.key==='End'){e.preventDefault();show(slides.length-1);}if(e.key.toLowerCase()==='n')toggle.click();});
  window.addEventListener('resize',fit);show(current);
})();
