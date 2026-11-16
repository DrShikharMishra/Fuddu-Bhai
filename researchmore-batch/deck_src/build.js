const {newDeck,renderSpec,save}=require('./lib');const fs=require('fs');
(async()=>{for(const f of process.argv.slice(2)){const d=require('./'+f);const {pres,C}=newDeck(d.no,d.title);
 for(const sec of d.sections){pres.addSection({title:sec.sec});renderSpec(pres,C,sec.spec,sec.sec);}
 await save(pres,`../decks/Day${d.no}_${d.title.replace(/[^A-Za-z]+/g,'_')}.pptx`);console.log('saved',d.no);}})();
