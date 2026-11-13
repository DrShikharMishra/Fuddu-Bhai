"""Voiceover with the open-source Kokoro model. usage: python3 tts.py <model_dir> [voice] [speed]"""
import os, sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
from timeline import LINES, HERE
md = sys.argv[1]; voice = sys.argv[2] if len(sys.argv) > 2 else "am_michael"; speed = float(sys.argv[3]) if len(sys.argv) > 3 else 1.1
npz = os.path.join(md, "voices.npz")
np.savez(npz, **{f[:-4]: np.fromfile(os.path.join(md, f), dtype=np.float32).reshape(-1, 1, 256) for f in os.listdir(md) if f.endswith(".bin")})
k = Kokoro(os.path.join(md, "kokoro.onnx"), npz)
for i, text in enumerate(LINES):
    x, sr = k.create(text, voice=voice, speed=speed, lang="en-us")
    nz = np.where(np.abs(x) > 0.01)[0]; x = x[max(0, nz[0] - 400): nz[-1] + 1800]   # trim silence
    sf.write(os.path.join(HERE, "build", f"vo{i}.wav"), x, sr); print(i, round(len(x) / sr, 2), text)
