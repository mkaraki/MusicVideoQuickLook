#!/usr/bin/env bash
FADE_DURATION=3
FONT='C\:/WINDOWS/Fonts/meiryo.ttc'

if [ $# -ne 7 ]; then
    echo "Usage: $0 <start_sec> <end_sec> <title/artist> <information> <information2 (empty to ignore)> <input_video> <output_path>"
    exit 1
fi

START_SEC=$1
END_SEC=$2
TITLE=$3
INFORMATION=$4
INFORMATION2=$5
INPUT=$6
OUTPUT=$7

if [[ "$INFORMATION2" == "" ]]; then
    INFORMATION2="$INFORMATION"
fi

FADEOUT_START=$((END_SEC - FADE_DURATION))

INFO1_END=$((START_SEC + FADE_DURATION + 5))

ffmpeg -i $INPUT \
    -vf "
        format=yuv444p
        ,drawbox=
            y=ih-150 :
            w=iw :
            h=150 :
            t=fill :
            color=black@0.4 :
            enable='between(t,$START_SEC,$END_SEC)'
        ,drawtext=
            fontfile='$FONT' :
            text='$TITLE' :
            fontcolor=white :
            fontsize=64 :
            x=25 :
            y=h-130 :
            enable='between(t,$START_SEC,$END_SEC)'
        ,drawtext=
            fontfile='$FONT' :
            text='$INFORMATION' :
            fontcolor=white :
            fontsize=32 :
            x=25 :
            y=h-55 :
            enable='between(t,$START_SEC,$INFO1_END)'
        ,drawtext=
            fontfile='$FONT' :
            text='$INFORMATION2' :
            fontcolor=white :
            fontsize=32 :
            x=25 :
            y=h-55 :
            enable='between(t,$INFO1_END,$END_SEC)'
        ,format=yuv420p
        ,fade=
            t=in :
            st=$START_SEC :
            d=$FADE_DURATION
        ,fade=
            t=out :
            st=$FADEOUT_START :
            d=$FADE_DURATION
        " \
    -af "afade=t=in:st=$START_SEC:d=$FADE_DURATION,afade=t=out:st=$FADEOUT_START:d=$FADE_DURATION" \
    -ss $START_SEC -to $END_SEC \
    $OUTPUT