#!/usr/bin/env bash
FADE_DURATION=3

if [ $# -ne 4 ]; then
    echo "Usage: $0 <start_sec> <end_sec> <input_video> <output_path>"
    exit 1
fi

START_SEC=$1
END_SEC=$2
INPUT=$3
OUTPUT=$4

ffmpeg -i $INPUT -ss $START_SEC -to $END_SEC -vf "fade=t=in:st=$START_SEC:d=$FADE_DURATION,fade=t=out:st=$END_SEC:d=$FADE_DURATION" -af "afade=t=in:st=$START_SEC:d=$FADE_DURATION,afade=t=out:st=$END_SEC:d=$FADE_DURATION" $OUTPUT