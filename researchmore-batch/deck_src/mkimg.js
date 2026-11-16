const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
const F=JSON.parse(fs.readFileSync('../src/figs.json'));
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:3});
for(const [k,v] of Object.entries(F)){
 const m=v.match(/viewBox="0 0 (\d+) (\d+)"/);const w=+m[1],h=+m[2];
 await p.setViewportSize({width:w,height:h});
 await p.setContent(`<body style="margin:0;background:#fff">${v.replace('<svg ',`<svg width="${w}" height="${h}" `)}</body>`);
 await p.screenshot({path:`../img/${k}.png`,clip:{x:0,y:0,width:w,height:h}});}
await b.close();console.log('ok')})();
