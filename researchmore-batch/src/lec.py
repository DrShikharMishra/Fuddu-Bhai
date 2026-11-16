D=[]
def day(n,title,obj,run,slides,demo,task,mist):D.append((n,title,obj,run,slides,demo,task,mist))
day(1,"Ask a good question",["Distinguish SR, MA and NMA and say when each is justified","Write a PICO(S) question with one primary outcome and time point","Write eligibility criteria with a reason for each rule","Know what PRISMA-P and PROSPERO require"],
[("0:00","10","Welcome, ground rules: teaching only, you write it"),("0:10","20","Concept: SR vs MA vs NMA; evidence hierarchy"),("0:30","30","PICO workshop: bad question → good question"),("1:00","15","Break + pair-share your draft PICO"),("1:15","25","Eligibility criteria and effect measure"),("1:40","30","Protocol structure, PRISMA-P, PROSPERO demo"),("2:10","20","Hands-on start, Q&amp;A, homework")],
[("The promise","Seven days, one protocol written by you.","Nobody here is getting a paper written for them. By Friday you can defend every line of your protocol. That's the product."),
("Three methods, one ladder","SR = method; MA = statistics inside an SR; NMA = many treatments at once. Pairwise first, network last.","Think of it as a ladder. You can't climb to the network without standing on the pairwise rung."),
("PICO, live","Take a vague question from the room. Rewrite on the board as P, I, C, O, S + primary outcome + time point.","Watch what happens to 'Does laparoscopy help?' when I ask: help whom, compared to what, measured how, when?"),
("Eligibility with reasons","Table: Design · Population · Intervention · Outcome · Other. Every row needs a justification.","If you can't explain a restriction to a sceptical reviewer, delete it. Language limits are the usual offender."),
("Effect measures decided now","RR/OR/RD · MD/SMD · HR; log scale for ratios.","Choose the measure before you see data, or you'll choose the one that looks best."),
("Protocol and registration","PRISMA-P: 17 items. PROSPERO before screening. OSF if ineligible.","A protocol is a promise you make before you can cheat. Registration makes the promise public.")],
["Open PROSPERO, search your topic, show how to read the records of existing reviews.","Show the PRISMA-P checklist and map its items onto the protocol template (Notes §7.4).","Demonstrate searching PubMed for 'systematic review' + topic to check duplicates."],
"Deliverable: PICO sentence + primary outcome with time point; 3 closest existing reviews with 1 line each on difference; eligibility table; Introduction + Objectives (150–250 words) of the protocol.",
["Outcome left vague","Registering after the work is done","Writing eligibility to fit the studies already known","Asking 'is X better than Y?' with no population"])
day(2,"Find everything",["Build a Boolean search with MeSH/Emtree and free text","Translate a strategy between databases","Run blinded dual screening in Rayyan","Produce a flow diagram whose numbers reconcile"],
[("0:00","10","Recap Day 1; check PICO homework"),("0:10","25","Concept: sensitivity vs precision; anatomy of a search"),("0:35","30","Live build: PubMed strategy line by line"),("1:05","15","Break"),("1:20","25","Embase/CENTRAL translation; registries; grey sources"),("1:45","25","Rayyan live: import, dedup, blind, conflicts"),("2:10","20","Hands-on start; Q&amp;A")],
[("Why searching is the review","Missed studies bias every number downstream.","We trade precision for sensitivity on purpose. Screening 1,000 to include 10 isn't failure, it's the design."),
("Concept blocks","P and I only; OR within, AND between; skip Outcome.","Searching the outcome hides studies that report it poorly in the abstract."),
("MeSH + free text","Controlled vocabulary catches indexed articles; text words catch the rest. Use both.","Show the PubMed MeSH Database; add entry terms to your free-text list."),
("Sources: MECCA","MEDLINE · Embase · CENTRAL · Citation chasing · And registries.","If a registry lists a finished trial with no paper, that's a missing study and a bias signal."),
("Check the search","PRESS peer review; PRISMA-S 16-item reporting; record date and interface.","Ask a librarian or a colleague to read your strategy. A typo can lose a whole concept."),
("Screening mechanics","Dedup → blind dual screen → conflict resolution; reasons for every full-text exclusion.","Pilot 50 records together. Disagreement at the pilot means the criteria need work, not the reviewers.")],
["PubMed: build #1 population block with MeSH + [tiab]; add #2 intervention; combine; check 5 golden papers appear.","Show the History tab and Search Details to prove the translation.","Rayyan: create review, upload RIS, detect duplicates, set blind ON, screen 10 records, toggle blind OFF to show conflicts.","Hand-fill the blank PRISMA flow from the numbers you just generated."],
"Deliverable: your PubMed strategy; one translated strategy; 100-record dual screen with agreement %; protocol sections Search + Selection.",
["Searching only PubMed","Bulk-deleting 'duplicates' without checking","Flow numbers that don't add","Single reviewer 'because it's faster'"])
day(3,"Judge the evidence",["Design and pilot an extraction form","Handle multi-arm trials and multiple reports","Apply RoB 2 (5 domains) and know ROBINS-I (7 domains)","Separate bias from imprecision and from poor reporting"],
[("0:00","10","Recap + screening check"),("0:10","25","Extraction: form, pilot, dual process, edge cases"),("0:35","20","Bias vs imprecision vs reporting"),("0:55","15","Break"),("1:10","35","RoB 2 walk-through with a real trial report"),("1:45","20","ROBINS-I and other tools"),("2:05","25","Hands-on: rate one trial in pairs")],
[("Extraction is design","Form → pilot → fix → extract. Source note for every number.","If a number has no page reference in your form, it doesn't exist."),
("Trial hygiene","One trial = one study; split or combine shared control arms.","Counting a control group twice makes your CI too narrow and your conclusion too bold."),
("Bias ≠ imprecision","Bias = systematic error; imprecision = random error.","A tiny perfect trial is unbiased but imprecise. A giant sloppy trial is the opposite."),
("RoB 2: R-D-M-M-S","Randomisation · Deviations · Missing data · Measurement · Selective reporting; Low / Some concerns / High.","Go domain by domain with signalling questions. Overall = worst domain."),
("ROBINS-I","7 domains; confounding is expected; compare to an ideal target trial.","Observational data rarely earn 'Low'. That's honest, not harsh."),
("Presenting RoB","Traffic-light and summary plots via robvis.","Colour is a summary. The reasons are written in the supporting table.")],
["Show an open trial paper; find allocation concealment, blinding, dropouts.","Compare outcomes in the paper vs the registry entry to demonstrate Domain 5.","robvis web app: paste a small CSV, produce a traffic-light plot."],
"Deliverable: extraction form (≤25 columns) piloted on 2 papers; RoB 2 on one outcome with a sentence of support per domain; disagreement log with a partner; protocol sections Data extraction + Risk of bias.",
["One 'quality score' by adding points","Judging the trial rather than the result","Excluding high-RoB trials silently","Mixing time points"])
day(4,"Pool it",["Explain inverse-variance weighting and the log scale","Choose and justify fixed vs random-effects","Interpret Q, τ², I² and prediction interval","Know when not to pool"],
[("0:00","10","Recap RoB; collect extraction forms"),("0:10","25","Concept: weighted average; effect measures"),("0:35","25","Fixed vs random; τ² and weights"),("1:00","15","Break"),("1:15","35","Worked example: six hypothetical trials, forest plot"),("1:50","20","R/RevMan demo"),("2:10","20","Hands-on: reproduce the example")],
[("A weighted average","Pooled = Σ w·y / Σ w ; w = 1/variance; ratios on the log scale.","The study with the tightest CI speaks loudest. Make that sentence second nature."),
("Two worldviews","Fixed: one true effect. Random: true effects vary with spread τ².","Ask: would I expect the same effect in rural India, Germany and a teaching hospital? Then random-effects is your default."),
("The worked example (Notes §4.3)","Q 9.13, τ² 0.108, I² 45%; FE RR 0.72 [0.54, 0.95], RE RR 0.68 [0.46, 1.02], PI 0.23–2.00.","Same data, two models, different significance. Don't pick the pleasing one. Report the pre-specified one and explain the gap."),
("Heterogeneity toolkit","Q, I² (overlapping bands), τ², prediction interval.","I² tells you the share of spread that's real. The prediction interval tells you what a new setting might show."),
("When not to pool","Clinical diversity, one study, or heterogeneity too large to average.","Not pooling is a result. Say why, then use structured narrative synthesis."),
("Software","metabin in R; RevMan; Jamovi.","Save the script. Your future self and every reviewer will ask for it.")],
["Open the 6-study dataset (CSV in the folder); compute log RR and SE in a spreadsheet.","R: run metabin with method.tau='REML', hakn=TRUE, prediction=TRUE; compare with DL.","Change Trial C events to 25 vs 30 and watch τ², I², and the FE vs RE gap shrink."],
"Deliverable: reproduce the pooled results; choose effect measure, model, τ² estimator and CI method for your own protocol and justify each in one line.",
["Choosing the model by I²","Reporting OR as if it were RR","Treating I² = 0 with k = 6 as proof of homogeneity","Silent 0.5 continuity corrections"])
day(5,"Stress-test it",["Plan subgroup and sensitivity analyses a priori","Interpret funnel plots and Egger's test with k ≥ 10","Apply GRADE: 5 downgrade, 3 upgrade","Draft a Summary of Findings row"],
[("0:00","10","Recap pooled result"),("0:10","25","Subgroups, meta-regression, sensitivity"),("0:35","25","Publication bias: funnel, Egger, trim-and-fill"),("1:00","15","Break"),("1:15","40","GRADE domains with worked examples"),("1:55","15","SoF table in GRADEpro"),("2:10","20","Hands-on: grade one outcome")],
[("Break your own result","Leave-one-out; exclude high RoB; model swaps; alternative measures.","If the conclusion flips, we say it flips. That's what stress-testing is for."),
("Subgroups, honestly","Pre-specify, few, test for subgroup difference, label post-hoc as exploratory.","Significant here and not there isn't a difference. Only the interaction test answers that."),
("Publication bias","Funnel plot, Egger, ≥10 studies, HERO causes of asymmetry.","Six studies and a symmetric funnel proves nothing. Look at registries instead."),
("GRADE: RIIPP ↓ LDC ↑","Start High for RCTs; five reasons down; three up.","Grade per outcome, and write the reason in a footnote, always."),
("Language of certainty","High · Moderate · Low · Very low with plain wording.","Low certainty = 'may'. Moderate = 'probably'. Words must match ratings."),
("Summary of Findings","Relative + absolute effect, N (studies), certainty, footnotes.","This table is the page the busy clinician reads. Make it honest.")],
["Leave-one-out in R (metainf); show Trial C's influence.","Funnel plot with 6 vs 12 studies to see the difference.","GRADEpro: create a SoF row from the Day 4 results."],
"Deliverable: leave-one-out on the Day 4 data; two pre-specified subgroups with reasons; GRADE rating for one outcome with a justification per domain; protocol sections on heterogeneity, sensitivity, bias, certainty.",
["Testing publication bias with <10 studies","Subgroup fishing","Grading the whole review as one","Downgrading with no footnote"])
day(6,"Go network",["Read network geometry","Judge transitivity from study characteristics","Interpret consistency checks, league tables and rankings","Rate confidence with CINeMA (6 domains)"],
[("0:00","10","Recap GRADE; check protocols so far"),("0:10","25","Concept: direct, indirect, mixed; geometry"),("0:35","25","Transitivity and consistency"),("1:00","15","Break"),("1:15","35","MetaInsight live demo: network plot, league table, SUCRA/P-score"),("1:50","25","CINeMA walk-through"),("2:15","15","Hands-on start")],
[("Why a network?","Many treatments, few head-to-head trials.","Clinicians must choose among five drugs. Pairwise MAs give ten separate answers; a network gives one coherent set."),
("Indirect = subtract","d(A,B) = d(A,Pl) − d(B,Pl).","It's algebra, but it's only valid if the trials are comparable."),
("Transitivity first","Effect modifiers must be similarly distributed across comparisons.","Build the transitivity table before you open the software."),
("Consistency second","Global design-by-treatment test; local node-splitting.","A non-significant test with few loops is low power, not reassurance."),
("League table + ranks","League table is primary; SUCRA/P-score never walks alone.","If someone says 'drug X is best' from a SUCRA, ask for the estimate, CI and certainty."),
("CINeMA","Within-study bias · Reporting bias · Indirectness · Imprecision · Heterogeneity · Incoherence.","Six ticks per comparison. It's tedious by design.")],
["MetaInsight: load example data; show network plot; league table; ranking panel.","Show node-split output; find a comparison with direct vs indirect disagreement.","CINeMA: upload sample; walk through contribution matrix and domain judgements."],
"Deliverable: your network sketch; a transitivity table (3 effect modifiers × comparisons); node definitions; the NMA section of your protocol.",
["Ranking without estimates","Lumping unlike treatments into one node","Skipping transitivity because the test is non-significant","Starting with NMA when pairwise is messy"])
day(7,"Write it up",["Match items to PRISMA-P, PRISMA 2020, PRISMA-NMA and PRISMA-S","Write results in language matched to certainty","Assemble and register the capstone protocol","Peer-review a protocol like a journal reviewer"],
[("0:00","10","Recap; bring protocol draft"),("0:10","30","The PRISMA family and report structure"),("0:40","25","Writing results and discussion; certainty language"),("1:05","15","Break"),("1:20","30","Capstone assembly against the template"),("1:50","30","Peer review round (swap protocols)"),("2:20","20","Live Q&amp;A; next steps")],
[("Which checklist when","P protocol (17) · 2020 main (27 + 12 abstract) · NMA (32) · S search (16).","Journals want page numbers beside every item. Keep a running map as you write."),
("Structure","Title, abstract, intro, methods, results, discussion, other.","Methods say what you planned and what changed. Results say what you found, all of it."),
("Words match certainty","'May reduce' for low; 'probably reduces' for moderate; 'no clear evidence' when the CI spans both.","Overclaiming is how a good review becomes a bad paper."),
("The capstone","Sixteen sections; registered; reviewed by a peer.","This is the thing you take home. Everything else is scaffolding."),
("Ethics and authorship","ICMJE criteria; disclose tools; verify every citation yourself.","If you couldn't defend a sentence in front of the editor, it doesn't go in."),
("What next","Register, screen, extract, analyse, report.","The batch ends. The review begins.")],
["Walk through the PRISMA 2020 checklist against a published review; find 3 missing items.","Demonstrate PROSPERO form completion section by section (no submission in class).","Peer review rubric: PICO clarity, reasons for eligibility, search completeness, pre-specified analyses, certainty plan."],
"Deliverable (capstone): complete protocol using the template; PRISMA-P checklist with section references; registry-ready text; one page of peer-review feedback received and one page of changes made.",
["Writing conclusions stronger than the evidence","Hiding deviations","Selective reporting of results","Treating registration as a formality"])
def build():
    o=[]
    for n,t,obj,run,sl,demo,task,mist in D:
        o.append(f"<section class='chap'><div class='opener' style='min-height:60mm'><div class='no'>{n}</div><div class='kick'>Lecture script · Day {n}</div><h1>{t}</h1><span class='hand'>hands-on task every day. not just a lecture to watch.</span></div>")
        o.append("<h3>Learning objectives</h3><ul>"+"".join(f"<li>{x}</li>" for x in obj)+"</ul>")
        o.append("<h3>Timed run-sheet (≈ 2 h 30 min; adjust to mode and organiser's timing)</h3><table><tr><th>Start</th><th>Min</th><th>Block</th></tr>"+"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in run)+"</table>")
        o.append("<h3>Slide-by-slide script</h3>")
        for i,(h,b,s) in enumerate(sl,1):
            o.append(f"<div class='sl'><div class='h'><span>Slide {i} · {h}</span><i>Day {n}</i></div><div class='b'><ul><li>{b}</li></ul><div class='say'>{s}</div></div></div>")
        o.append("<div class='box mn'><span class='t'>Live demo steps</span><ol>"+"".join(f"<li>{x}</li>" for x in demo)+"</ol></div>")
        o.append(f"<div class='box task'><span class='t'>Hands-on task</span><p>{task}</p></div>")
        o.append("<div class='box trap'><span class='t'>Common mistakes to watch for</span><ul>"+"".join(f"<li>{x}</li>" for x in mist)+"</ul></div></section>")
    return "".join(o)
open('l1.html','w').write(build())
for i in range(2,8): open(f'l{i}.html','w').write('')
