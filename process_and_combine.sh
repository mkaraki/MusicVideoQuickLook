#!/usr/bin/env bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <video list> <output_path>"
    exit 1
fi

videolist=$1
combined_output=$2

tempfile="temp-video-list.list"
echo -n "" > $tempfile

while read row; do
    inputfile=`echo ${row} | cut -d , -f 1`
    if [[ "$inputfile" == "Input" ]]; then
        continue
    fi

    filename=$(basename -- "$inputfile")
    ext="${filename##*.}"

    title=`echo ${row} | cut -d , -f 2`
    information1=`echo ${row} | cut -d , -f 3`
    information2=`echo ${row} | cut -d , -f 4`
    startsec=`echo ${row} | cut -d , -f 5`
    endsec=`echo ${row} | cut -d , -f 6`

    outputfile=$inputfile.feded.$ext

    echo "file '$outputfile'" >> $tempfile

    ./gen_feded_video_with_text.sh "$startsec" "$endsec" "$title" "$information1" "$information2" "$inputfile" "$outputfile"

done < $videolist

ffmpeg -f concat -safe 0 -i $tempfile $combined_output

rm $tempfile