// Renders frames of reel.html with Playwright and pipes them to ffmpeg.
// usage: node render.js [--stills t1,t2,...]  -> build/video.mp4 or build/still_*.jpg
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path'); const { spawn } = require('child_process');
(async () => {
  const T = JSON.parse(fs.readFileSync(path.join(__dirname, 'build/timeline.json')));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  p.on('pageerror', e => { console.error('PAGE ERROR', e.message); process.exit(1); });
  await p.goto('file://' + path.join(__dirname, 'reel.html'));
  await p.evaluate(async T => { setTimeline(T); await document.fonts.load('900 96px "Inter Display"'); await document.fonts.load('800 46px "Inter Display"'); }, T);
  const grab = t => p.evaluate(t => { renderAt(t); return document.getElementById('c').toDataURL('image/jpeg', 0.93).split(',')[1]; }, t);
  const si = process.argv.indexOf('--stills');
  if (si > 0) { for (const t of process.argv[si + 1].split(',').map(Number)) fs.writeFileSync(path.join(__dirname, `build/still_${t.toFixed(2)}.jpg`), Buffer.from(await grab(t), 'base64')); }
  else {
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', '-pix_fmt', 'yuv420p', path.join(__dirname, 'build/video.mp4')], { stdio: ['pipe', 'inherit', 'inherit'] });
    const n = Math.round(T.dur * 30);
    for (let f = 0; f < n; f++) { const buf = Buffer.from(await grab(f / 30), 'base64'); if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r)); if (f % 150 == 0) console.log('frame', f, '/', n); }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
  }
  await b.close();
})();
