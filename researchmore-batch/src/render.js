const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const n of process.argv.slice(2)){
 const p=await b.newPage();await p.goto('file://'+process.cwd()+'/../notes/'+n+'.html');await p.evaluate(()=>document.fonts.ready);
 await p.pdf({path:'../notes/'+n+'.pdf',format:'A4',printBackground:true,displayHeaderFooter:true,margin:{top:'16mm',bottom:'17mm',left:'15mm',right:'15mm'},
 headerTemplate:'<div></div>',footerTemplate:`<div style="width:100%;font:7pt Courier;color:#5b6479;padding:0 15mm;display:flex;justify-content:space-between"><span>RESEARCHMORE · SR · MA · NMA · SESSION NOTES</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`});
 await p.close()}
await b.close()})();
