const pptxgen=require('pptxgenjs');const fs=require('fs');
const {applyTheme}=require(require('child_process').execSync("ls -d /root/.claude/skills/synced/*/pptx/scripts/apply_theme.js").toString().trim());
const THEME={name:"Researchmore Academic",headFontFace:"Times New Roman",bodyFontFace:"Arial",colors:{dk1:"1B2238",lt1:"FFFFFF",dk2:"0F2A4A",lt2:"EAF0F8",accent1:"C8102E",accent2:"0F2A4A",accent3:"3D66B8",accent4:"2F7D4F",accent5:"B8892B",accent6:"5B6479",hlink:"3D66B8",folHlink:"5B6479"}};
const HEX={navy:"0F2A4A",red:"C8102E",ice:"EAF0F8",blue:"3D66B8",green:"2F7D4F",gold:"B8892B",mute:"5B6479",ink:"1B2238"};
const IMG=(n)=>{const s=require('child_process').execSync(`python3 -c "from PIL import Image;i=Image.open('../img/${n}.png');print(i.size[0],i.size[1])"`).toString().trim().split(' ');return {path:`../img/${n}.png`,r:s[0]/s[1]}};
function newDeck(dayNo,dayTitle){
 const pres=new pptxgen();pres.layout='LAYOUT_WIDE';pres.theme={headFontFace:THEME.headFontFace,bodyFontFace:THEME.bodyFontFace};
 pres.title=`Day ${dayNo} · ${dayTitle}`;pres.author="Researchmore Publications";pres.company="Researchmore Publications";
 const C={text1:"1B2238",text2:"0F2A4A",background1:"FFFFFF",background2:"EAF0F8",accent1:"C8102E",accent3:"3D66B8",accent4:"2F7D4F",accent5:"B8892B",accent6:"5B6479"};
 pres.defineSlideMaster({title:"CONTENT",background:{color:C.background1},
  objects:[{text:{text:`SR · MA · NMA Teaching Batch  |  Day ${dayNo}`,options:{x:0.6,y:7.05,w:8,h:0.3,fontSize:10,color:C.accent6,margin:0}}},
           {text:{text:"Researchmore Publications",options:{x:8.7,y:7.05,w:3.5,h:0.3,fontSize:10,color:C.accent6,align:'right',margin:0}}},
           {placeholder:{options:{name:"title",type:"title",x:0.6,y:0.35,w:12.1,h:0.95,fontSize:32,bold:true,color:C.text2,fontFace:"Times New Roman",valign:'middle',align:'left',margin:0},text:""}}],
  slideNumber:{x:12.3,y:7.05,w:0.5,h:0.3,fontSize:10,color:C.accent6,align:'right'}});
 pres.defineSlideMaster({title:"DARK",background:{color:C.text2},objects:[
  {placeholder:{options:{name:"title",type:"title",x:0.9,y:2.3,w:11.5,h:1.8,fontSize:48,bold:true,color:C.background1,fontFace:"Times New Roman",valign:'top',align:'left',margin:0},text:""}}]});
 return {pres,C};
}
function cardsBg(s,C,x,y,w,h,fill){s.addShape('roundRect',{x,y,w,h,rectRadius:0.08,fill:{color:fill||C.background2},line:{color:fill||C.background2,width:0}});}
function T(s,txt,o){s.addText(txt,Object.assign({isTextBox:true,margin:0,fontFace:"Arial"},o));}
const bl=(a,o={})=>a.map((t,i)=>({text:t,options:Object.assign({bullet:true,breakLine:i<a.length-1,paraSpaceAfter:8},o)}));
function renderSpec(pres,C,spec,sec){
 for(const sp of spec){
  if(sp.k==='title'){const s=pres.addSlide({masterName:"DARK",sectionTitle:sec});
   T(s,sp.kicker,{x:0.9,y:1.4,w:11,h:0.4,fontSize:16,color:C.background2,bold:true,charSpacing:4});
   s.addText(sp.title,{placeholder:"title"});
   T(s,sp.sub,{x:0.9,y:4.4,w:10.5,h:1.2,fontSize:22,color:C.background2});
   T(s,"Researchmore Publications  ·  Teaching batch: SR · MA · NMA  ·  Teaching only, not a writing service",{x:0.9,y:6.7,w:11.5,h:0.35,fontSize:12,color:C.background2});
   if(sp.n)s.addNotes(sp.n);continue;}
  if(sp.k==='divider'){const s=pres.addSlide({masterName:"DARK",sectionTitle:sec});
   T(s,sp.kicker||"",{x:0.9,y:1.6,w:11,h:0.4,fontSize:16,color:C.accent1,bold:true});
   s.addText(sp.title,{placeholder:"title"});T(s,sp.sub||"",{x:0.9,y:4.3,w:10.5,h:1.4,fontSize:22,color:C.background2});if(sp.n)s.addNotes(sp.n);continue;}
  const s=pres.addSlide({masterName:"CONTENT",sectionTitle:sec});s.addText(sp.title,{placeholder:"title"});
  const y0=1.5,H=5.3;
  if(sp.k==='bul'){ // bullets left, optional image or callout right
   const hasR=sp.img||sp.call;const w=hasR?6.2:12.1;
   T(s,bl(sp.b,{paraSpaceAfter:12}),{x:0.6,y:y0,w,h:H,fontSize:21,color:C.text1,valign:'top'});
   if(sp.img){const im=IMG(sp.img);let iw=5.7,ih=iw/im.r;if(ih>H-0.2){ih=H-0.2;iw=ih*im.r}
     s.addImage({path:im.path,x:7.0+(5.7-iw)/2,y:y0+(H-ih)/2,w:iw,h:ih,altText:sp.alt||sp.title,objectName:"Figure"});}
   if(sp.call){cardsBg(s,C,7.0,y0,5.7,3.6,C.background2);
     T(s,sp.call.h,{x:7.3,y:y0+0.25,w:5.1,h:0.5,fontSize:14,bold:true,color:C.accent1,charSpacing:2});
     T(s,sp.call.t,{x:7.3,y:y0+0.8,w:5.1,h:2.6,fontSize:20,color:C.text2,valign:'top'});}}
  if(sp.k==='img'){const im=IMG(sp.img);const mh=sp.cap?4.7:H-0.1;let iw=11.5,ih=iw/im.r;if(ih>mh){ih=mh;iw=ih*im.r}
   s.addImage({path:im.path,x:(13.33-iw)/2,y:y0,w:iw,h:ih,altText:sp.alt||sp.title,objectName:"Figure"});
   if(sp.cap)T(s,sp.cap,{x:0.8,y:y0+ih+0.25,w:11.7,h:0.9,fontSize:16,color:C.text2,valign:'top'});}
  if(sp.k==='tbl'){const hd=sp.h.map(t=>({text:t,options:{bold:true,color:C.background1,fill:{color:C.text2},fontSize:17,fontFace:"Arial"}}));
   const rows=[hd].concat(sp.r.map((r,i)=>r.map((c,j)=>({text:c,options:{fontSize:sp.fs||17,color:(sp.hl&&sp.hl.includes(j))?C.accent1:C.text1,bold:j===0||(sp.hl&&sp.hl.includes(j)),fill:{color:i%2?C.background2:C.background1},fontFace:"Arial"}}))));
   s.addTable(rows,{x:0.6,y:y0,w:12.1,colW:sp.cw,border:{type:'solid',pt:0.75,color:C.background2},margin:[6,10,6,10],valign:'middle',autoPage:false,rowH:sp.rh||0.72});
   if(sp.foot)T(s,sp.foot,{x:0.6,y:6.3,w:12.1,h:0.6,fontSize:16,color:C.accent1,bold:true,valign:'top'});}
  if(sp.k==='cards'){const n=sp.c.length,g=0.3,w=(12.1-g*(n-1))/n;
   sp.c.forEach((c,i)=>{const x=0.6+i*(w+g);cardsBg(s,C,x,y0,w,4.2,C.background2);
    s.addShape('ellipse',{x:x+0.3,y:y0+0.3,w:0.6,h:0.6,fill:{color:C.accent1},line:{color:C.accent1,width:0}});
    T(s,String(c.n||i+1),{x:x+0.3,y:y0+0.3,w:0.6,h:0.6,fontSize:18,bold:true,color:C.background1,align:'center',valign:'middle'});
    T(s,c.h,{x:x+0.3,y:y0+1.1,w:w-0.6,h:0.8,fontSize:n>=6?13:n>=5?16:19,bold:true,color:C.text2,valign:'top',fontFace:"Times New Roman"});
    T(s,c.t,{x:x+0.3,y:y0+1.95,w:w-0.6,h:2.1,fontSize:n>=5?14:17,color:C.text1,valign:'top'});});
   if(sp.foot)T(s,sp.foot,{x:0.6,y:6.0,w:12.1,h:0.6,fontSize:18,color:C.accent1,bold:true,valign:'top'});}
  if(sp.k==='flow'){const n=sp.c.length,g=0.25,w=(12.1-g*(n-1))/n;
   sp.c.forEach((c,i)=>{const x=0.6+i*(w+g);s.addShape('roundRect',{x,y:y0+0.3,w,h:1.1,rectRadius:0.08,fill:{color:i===n-1&&sp.last?C.accent1:C.text2},line:{color:C.text2,width:0}});
    T(s,c.h,{x:x+0.1,y:y0+0.3,w:w-0.2,h:1.1,fontSize:17,bold:true,color:C.background1,align:'center',valign:'middle',fontFace:"Times New Roman"});
    if(i<n-1)T(s,"›",{x:x+w-0.05,y:y0+0.55,w:g+0.1,h:0.6,fontSize:28,bold:true,color:C.accent1,align:'center'});
    T(s,c.t,{x:x,y:y0+1.7,w:w,h:2,fontSize:17,color:C.text1,valign:'top'});});
   if(sp.foot)T(s,sp.foot,{x:0.6,y:6.3,w:12.1,h:0.6,fontSize:16,color:C.accent1,bold:true,valign:'top'});}
  if(sp.k==='stat'){const n=sp.c.length,g=0.3,w=(12.1-g*(n-1))/n;
   sp.c.forEach((c,i)=>{const x=0.6+i*(w+g);cardsBg(s,C,x,y0,w,3.2,C.background2);
    T(s,c.v,{x:x+0.2,y:y0+0.3,w:w-0.4,h:1.3,fontSize:54,bold:true,color:C.accent1,align:'center',valign:'middle',fontFace:"Times New Roman"});
    T(s,c.l,{x:x+0.3,y:y0+1.7,w:w-0.6,h:1.3,fontSize:16,color:C.text2,align:'center',valign:'top'});});
   T(s,sp.b?bl(sp.b):"",{x:0.6,y:y0+3.5,w:12.1,h:1.7,fontSize:17,color:C.text1,valign:'top'});}
  if(sp.k==='chart'){const d=sp.data;
   s.addChart(pres.charts.BAR,d.series,{x:0.6,y:y0,w:7.2,h:H-0.2,barDir:'bar',chartColors:d.colors,showLegend:d.series.length>1,legendPos:'b',legendFontSize:14,legendColor:HEX.ink,legendFontFace:"+mn-lt",
    showValue:true,dataLabelFontSize:14,dataLabelColor:HEX.ink,dataLabelFontFace:"+mn-lt",dataLabelFormatCode:d.fmt||'0.0',catAxisLabelFontSize:14,catAxisLabelColor:HEX.ink,catAxisLabelFontFace:"+mn-lt",valAxisLabelFontSize:12,valAxisLabelColor:HEX.mute,valAxisLabelFontFace:"+mn-lt",valGridLine:{color:"D9E1EC",size:0.5},catGridLine:{style:'none'},showTitle:true,title:d.title,titleFontSize:15,titleColor:HEX.navy,titleFontFace:"+mn-lt",catAxisOrientation:d.rev?'maxMin':'minMax',valAxisMinVal:d.min,valAxisMaxVal:d.max,barGapWidthPct:60});
   cardsBg(s,C,8.1,y0,4.6,H-0.2,C.background2);T(s,sp.read.h,{x:8.4,y:y0+0.25,w:4.0,h:0.5,fontSize:14,bold:true,color:C.accent1,charSpacing:2});
   T(s,bl(sp.read.b),{x:8.4,y:y0+0.85,w:4.0,h:H-1.4,fontSize:16,color:C.text1,valign:'top'});}
  if(sp.k==='task'){cardsBg(s,C,0.6,y0,12.1,H-0.2,C.background2);
   T(s,"DELIVERABLES",{x:1.0,y:y0+0.3,w:6,h:0.4,fontSize:14,bold:true,color:C.accent1,charSpacing:3});
   sp.b.forEach((t,i)=>{const yy=y0+0.95+i*1.0;s.addShape('ellipse',{x:1.0,y:yy,w:0.55,h:0.55,fill:{color:C.accent4},line:{color:C.accent4,width:0}});
    T(s,String(i+1),{x:1.0,y:yy,w:0.55,h:0.55,fontSize:16,bold:true,color:C.background1,align:'center',valign:'middle'});
    T(s,t,{x:1.8,y:yy-0.05,w:10.5,h:0.8,fontSize:17,color:C.text1,valign:'middle'});});}
  if(sp.k==='quiz'){sp.q.forEach((q,i)=>{const yy=y0+i*1.65;cardsBg(s,C,0.6,yy,12.1,1.5,C.background2);
    T(s,`Q${i+1}`,{x:0.9,y:yy+0.1,w:0.8,h:1.3,fontSize:24,bold:true,color:C.accent1,valign:'middle',fontFace:"Times New Roman"});
    T(s,[{text:q[0],options:{bold:true,breakLine:true,fontSize:19,color:HEX.navy}},{text:q[1],options:{fontSize:17,color:HEX.ink}}],{x:1.8,y:yy+0.1,w:10.6,h:1.3,valign:'middle'});});}
  if(sp.k==='code'){cardsBg(s,C,0.6,y0,7.3,H-0.2,C.text2);T(s,sp.code,{x:0.9,y:y0+0.3,w:6.7,h:H-0.8,fontSize:15,color:C.background1,fontFace:"Courier New",valign:'top'});
   cardsBg(s,C,8.2,y0,4.5,H-0.2,C.background2);T(s,sp.read.h,{x:8.5,y:y0+0.25,w:4,h:0.5,fontSize:14,bold:true,color:C.accent1,charSpacing:2});T(s,bl(sp.read.b),{x:8.5,y:y0+0.85,w:3.9,h:H-1.4,fontSize:16,color:C.text1,valign:'top'});}
  if(sp.k==='img2'){const a=IMG(sp.img[0]),b=IMG(sp.img[1]);const mh=3.9;[a,b].forEach((im,i)=>{let iw=5.8,ih=iw/im.r;if(ih>mh){ih=mh;iw=ih*im.r}
    s.addImage({path:im.path,x:0.6+i*6.3+(5.8-iw)/2,y:y0,w:iw,h:ih,altText:sp.cap[i],objectName:"Figure"+(i+1)});T(s,sp.cap[i],{x:0.6+i*6.3,y:y0+4.0,w:5.8,h:0.5,fontSize:16,bold:true,color:C.text2,align:'center'});});
   T(s,sp.foot,{x:0.6,y:6.1,w:12.1,h:0.8,fontSize:17,color:C.accent1,bold:true,valign:'top'});}
  if(sp.n)s.addNotes(sp.n);
 }}
async function save(pres,name){await pres.writeFile({fileName:name});}
module.exports={newDeck,renderSpec,save,HEX,THEME};
