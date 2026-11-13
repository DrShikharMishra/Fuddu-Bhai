#!/bin/bash
set -e; cd "$(dirname "$0")"
ffmpeg -y -loglevel error -i build/video.mp4 -i build/mix.wav -c:v copy -af "loudnorm=I=-14:TP=-1" -c:a aac -b:a 192k -ar 44100 -shortest -movflags +faststart foot-asleep.mp4
echo built foot-asleep.mp4
