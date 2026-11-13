# Reel 01 — Why your foot "falls asleep"

**Format:** 1080x1920, 30 fps, ~33 s, narrated explainer with karaoke captions.
**Concept:** "Glass Leg" — an x-ray glass limb you dive *into*; the nerve is the main character.

## Script (voiceover)
1. When your foot falls asleep, it's not because the blood got cut off. *(hook: myth-bust)*
2. Sitting like this squashes a nerve in your leg, along with the tiny vessels that feed it.
3. Starved of oxygen, the nerve stops sending signals, so your brain hears nothing, and your foot goes numb.
4. But the moment you move, the pressure lifts, and the nerve starts to reboot.
5. Its fibres switch back on out of sync, firing random bursts all at once.
6. Your brain can't make sense of the chaos, so it feels like pins and needles.
7. So that annoying tingle is actually your nerve coming back online. *(payoff: reframe)*

## Fact check
- Numbness comes from compression of a peripheral nerve and of the small vessels supplying it
  (vasa nervorum); the main arteries to the foot stay open.
- "Pins and needles" (transient paraesthesia) happens as the nerve recovers: fibres fire
  spontaneous, disorganised bursts that the brain reads as tingling.
- Harmless when brief. Persistent or recurrent numbness needs a medical review.

## Beat sheet
| # | Line | Visual | On-screen text | Transition / FX | Sound |
|---|------|--------|----------------|-----------------|-------|
| 1 | 1 | Glass leg, foot greys out, Zzz, blood still flowing | BLOOD CUT OFF? -> struck, NOPE stamp | punch zoom-out, flash | whoosh, stamp thud |
| 2 | 2a | Other leg drops onto calf, pinch rings on nerve | SQUASHED | shake on impact | thud |
| 3 | 2b | Zoom THROUGH the skin: nerve tube squeezed, vessels drain | NERVE / TINY BLOOD VESSELS | zoom-through + flash | whoosh |
| 4 | 3 | Signals stall at the pinch, nerve goes grey; brain monitor flatlines | NO OXYGEN, NO SIGNAL, NUMB | music cuts to heartbeat | power-down sweep |
| 5 | 4 | Pressure releases, blood rushes back, nerve flickers | REBOOTING 0-100% | flash + shake | riser, ping |
| 6 | 5 | Fibres misfire in random colours, arcs | OUT OF SYNC | glitch | crackle |
| 7 | 6 | Chaos races up leg to brain monitor; whip to foot: sparks + needles (signature moment) | SIGNAL: ??? | glitch, whip zoom, shake | crackle, tinkles |
| 8 | 7 | Ordered pulses, warm foot, monitor green; end card | BACK ONLINE, FOLLOW | flash | chime |

## Rebuild
```
python3 tts.py <dir with kokoro.onnx + voice .bin files> am_michael 1.1   # voiceover -> build/vo*.wav
python3 timeline.py     # word timings + event cues -> build/timeline.json
python3 audio.py        # music + sfx + voice -> build/mix.wav
node render.js          # frames -> build/video.mp4
bash build.sh           # mux -> foot-asleep.mp4
```
