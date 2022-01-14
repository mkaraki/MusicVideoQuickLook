#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <video list>"
    exit 1
fi

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

    ./gen_feded_video_with_text.sh "$startsec" "$endsec" "$title" "$information1" "$information2" "$inputfile" "$outputfile"

done < $1