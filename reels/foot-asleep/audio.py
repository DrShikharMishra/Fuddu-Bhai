"""Synthesises the music bed + sound effects and mixes them with the voiceover -> build/mix.wav"""
import json, os, numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, "build")
T = json.load(open(os.path.join(B, "timeline.json"))); E = T["ev"]; L = T["lines"]
SR = 44100; N = int(T["dur"] * SR); rng = np.random.default_rng(7)
def tt(d): return np.arange(int(d * SR)) / SR
def lp(x, n): return np.convolve(x, np.ones(n) / n, mode="same") if n > 1 else x
def put(buf, x, at, g=1.0):
    i = int(at * SR)
    if i >= len(buf) or i < 0: return
    x = x[: len(buf) - i]; buf[i:i + len(x)] += x * g
def env(n, a=0.005, r=0.2):
    e = np.ones(n); na = max(1, int(a * SR)); nr = max(1, min(n - na, int(r * SR)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] = np.linspace(1, 0, nr) ** 2; return e
def note(f, d, kind="pluck"):
    t = tt(d)
    if kind == "bass": return (np.sin(2*np.pi*f*t) + .35*np.sin(4*np.pi*f*t)) * np.exp(-t*5) * env(len(t), .004, .05)
    return (np.sin(2*np.pi*f*t) + .4*np.sin(2*np.pi*2*f*t) + .15*np.sin(2*np.pi*3*f*t)) * np.exp(-t*9) * env(len(t), .002, .05)
def kick(): t = tt(.28); return np.sin(2*np.pi*(45*t + 60*(1-np.exp(-t*30))/30)) * np.exp(-t*14)
def hat(): t = tt(.05); x = rng.standard_normal(len(t)); return (x - lp(x, 6)) * np.exp(-t*90)
def whoosh(d=.45, up=True):
    t = tt(d); x = rng.standard_normal(len(t)); k = np.linspace(0, 1, len(t)); k = k if up else 1 - k
    y = lp(x, 40) * (1 - k) + (x - lp(x, 8)) * k * .6 + lp(x, 12) * .5
    return y * np.sin(np.pi * np.linspace(0, 1, len(t))) ** 2
def thud(): t = tt(.5); return np.sin(2*np.pi*(38*t + 90*(1-np.exp(-t*22))/22)) * np.exp(-t*7) + lp(rng.standard_normal(len(t)), 30) * np.exp(-t*40) * .8
def sweep(f0, f1, d, shape=1.0):
    t = tt(d); f = f0 * (f1 / f0) ** ((t / d) ** shape); ph = 2*np.pi*np.cumsum(f)/SR
    return (np.sin(ph) + .3*np.sign(np.sin(ph))) * env(len(t), .01, .12)
def crackle(d, dens=38):
    n = int(d * SR); y = np.zeros(n)
    for _ in range(int(d * dens)):
        i = rng.integers(0, n - 900); m = rng.integers(120, 800); x = rng.standard_normal(m)
        y[i:i+m] += (x - lp(x, 4)) * np.exp(-np.arange(m) / (m / 4)) * rng.uniform(.3, 1)
        f = rng.uniform(900, 3200); m2 = 700; y[i:i+m2] += np.sin(2*np.pi*f*np.arange(m2)/SR) * np.exp(-np.arange(m2)/120) * .35
    return y
def bell(fs, d=1.6): t = tt(d); return sum(np.sin(2*np.pi*f*t) * np.exp(-t*(3+i)) for i, f in enumerate(fs)) / len(fs)

# ---- music: 104 bpm pulse in A minor; drops out while the nerve is "dead" ----
music = np.zeros(N); bpm = 104; beat = 60 / bpm
roots = [110.0, 87.31, 130.81, 98.0]                # A2 F2 C3 G2
arps = [[220, 261.63, 329.63, 440], [174.61, 220, 261.63, 349.23], [261.63, 329.63, 392, 523.25], [196, 246.94, 293.66, 392]]
dead0, dead1 = E["block"], E["release"]
k = 0; t0 = 0.0
while t0 < T["dur"] - .2:
    bar = (k // 8) % 4; live = not (dead0 <= t0 < dead1) and t0 < E["end"] + .2
    if live:
        put(music, note(roots[bar], beat * .5, "bass"), t0, .55)
        put(music, note(arps[bar][(k * 3) % 4] * (2 if k % 8 in (3, 6) else 1), .3), t0, .16)
        if k % 2 == 0: put(music, kick(), t0, .6)
        else: put(music, hat(), t0, .12)
    elif k % 4 == 0:                                 # heartbeat while numb
        put(music, kick(), t0, .5); put(music, kick(), t0 + .22, .3)
    k += 1; t0 += beat / 2
td = tt(dead1 - dead0 + .4); put(music, np.sin(2*np.pi*55*td) * .12 * env(len(td), .4, .4), dead0)
music *= np.concatenate([np.ones(N - SR), np.linspace(1, 0, SR)])

# ---- sfx ----
sfx = np.zeros(N); S = [0.0] + [l["s"] for l in L[1:]]
put(sfx, whoosh(.5), 0, .5); put(sfx, thud(), E["nope"] + .2, .7)
put(sfx, whoosh(.45), E["press"] - .4, .45); put(sfx, thud(), E["press"], 1.0)
put(sfx, whoosh(.5), E["zoom"] - .3, .7)
put(sfx, sweep(520, 38, .9, .7), E["block"], .28)
put(sfx, thud(), E["numb"], .6)
put(sfx, whoosh(.6), E["release"] - .5, .6); put(sfx, sweep(120, 900, .5, 1.6), E["release"], .16); put(sfx, bell([660, 990], .7), E["release"], .18)
put(sfx, crackle(E["reboot"] + .5 - E["release"], 10), E["release"] + .2, .22)
put(sfx, crackle(S[5] - S[4], 42), S[4], .3)
put(sfx, crackle(E["pins"] - S[5], 26), S[5], .22); put(sfx, sweep(1800, 90, .4), E["chaos"], .14)
put(sfx, whoosh(.35), E["pins"] - .3, .6)
pins = crackle(S[6] - E["pins"], 30); t = np.arange(len(pins)) / SR
for i in range(int((S[6] - E["pins"]) * 14)): put(pins, bell([rng.uniform(2400, 4200)], .12), i / 14 + rng.uniform(0, .05), .35)
put(sfx, pins, E["pins"], .28)
put(sfx, whoosh(.4), S[6] - .3, .5); put(sfx, bell([523.25, 659.25, 783.99, 1046.5], 2.2), E["online"], .5)
put(sfx, whoosh(.5, False), E["end"] - .1, .4)

# ---- voice ----
vo = np.zeros(N); have = False
for i, l in enumerate(L):
    p = os.path.join(B, f"vo{i}.wav")
    if not os.path.exists(p): continue
    x, sr = sf.read(p); x = x.mean(1) if x.ndim > 1 else x
    x = np.interp(np.arange(int(len(x) * SR / sr)) * sr / SR, np.arange(len(x)), x); put(vo, x, l["s"]); have = True
if have: vo *= .95 / max(1e-6, np.abs(vo).max())
# duck music under the voice
duck = 1 - .55 * np.clip(lp(np.abs(vo), 6000) * 14, 0, 1) if have else 1
mix = vo * 1.0 + music * .34 * duck + sfx * .5
mix = np.tanh(mix * 1.15) * .92
sf.write(os.path.join(B, "mix.wav"), np.stack([mix, mix], 1), SR)
sf.write(os.path.join(B, "music_sfx.wav"), np.tanh((music * .34 + sfx * .5) * 1.15), SR)
print("mix written, voice:", have)
