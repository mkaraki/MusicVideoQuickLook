import ffmpeg
import sys
import os
import csv
import gen_feded_video_with_text
import process


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: process_and_combine.py <input csv> <output>")
        sys.exit(1)

    clips = []

    with open(sys.argv[1], encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if (row[0] == 'Input'):
                continue

            clips.append(process.ClipInfo(row[0], int(row[1]),
                         int(row[2]), row[3], row[4:]))

    streams = process.process_videos(clips, {'return_stream': True})

    print(streams)

    concat = ffmpeg.concat(*streams, v=1, a=1)
    concat.output(sys.argv[2]).run()

    exit
