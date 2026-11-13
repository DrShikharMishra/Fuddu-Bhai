"""Builds build/timeline.json from the script + (if present) real voiceover clip durations."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LINES = [
 "When your foot falls asleep, it's not because the blood got cut off.",
 "Sitting like this squashes a nerve in your leg, along with the tiny vessels that feed it.",
 "Starved of oxygen, the nerve stops sending signals, so your brain hears nothing, and your foot goes numb.",
 "But the moment you move, the pressure lifts, and the nerve starts to reboot.",
 "Its fibres switch back on out of sync, firing random bursts all at once.",
 "Your brain can't make sense of the chaos, so it feels like pins and needles.",
 "So that annoying tingle is actually your nerve coming back online.",
]
GAP, LEAD, TAIL = 0.14, 0.15, 1.6

def wav_dur(p):
    import soundfile as sf
    i = sf.info(p); return i.frames / i.samplerate

def build():
    t = LEAD; lines = []
    for i, text in enumerate(LINES):
        wav = os.path.join(HERE, "build", f"vo{i}.wav")
        d = wav_dur(wav) if os.path.exists(wav) else len(text) * 0.058
        words = text.split()
        wts = [len(re.sub(r"\W", "", w)) + 1.5 + (2.5 if w[-1] in ",." else 0) for w in words]
        tot = sum(wts); acc = 0; ws = []
        for w, wt in zip(words, wts):
            ws.append({"w": w, "s": round(t + d * acc / tot, 3), "e": round(t + d * (acc + wt) / tot, 3)}); acc += wt
        lines.append({"text": text, "s": round(t, 3), "e": round(t + d, 3), "words": ws})
        t += d + GAP
    def word(li, w, n=0):
        hits = [x for x in lines[li]["words"] if re.sub(r"\W", "", x["w"]).lower() == w]
        return hits[n]["s"]
    ev = {
        "blood": word(0, "blood"), "nope": word(0, "cut"),
        "press": lines[1]["s"] + 0.55, "zoom": word(1, "along"),
        "block": word(2, "stops"), "numb": word(2, "numb"),
        "release": word(3, "pressure"), "reboot": word(3, "reboot"),
        "chaos": word(5, "chaos"), "pins": word(5, "pins"),
        "online": word(6, "back"), "end": lines[-1]["e"] + 0.15,
    }
    T = {"lines": lines, "ev": ev, "dur": round(lines[-1]["e"] + TAIL, 3), "fps": 30}
    json.dump(T, open(os.path.join(HERE, "build", "timeline.json"), "w"), indent=1)
    return T

if __name__ == "__main__":
    T = build(); print("duration", T["dur"]); print(T["ev"])
