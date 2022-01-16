import sys
import os
import csv
import gen_feded_video_with_text


class ClipInfo:
    def __init__(self, infile, start, end, title, infos):
        self.input = infile

        _, ext = os.path.splitext(infile)

        self.output = infile + '.feded' + ext
        self.start = start
        self.end = end
        self.title = title
        self.infos = infos


def process_videos(videos, options=None):
    if (options == None):
        options = {}

    outputs = []
    for video in videos:
        stream = gen_feded_video_with_text.gentxtvid(
            video.input, video.output, video.start, video.end, video.title, video.infos, options)
        if ('return_stream' in options and options['return_stream']):
            outputs.extend(stream)
        else:
            outputs.append(video.output)
    return outputs


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: process_and_combine.py <input csv>")
        sys.exit(1)

    clips = []

    with open(sys.argv[1], encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if (row[0] == 'Input'):
                continue

            clips.append(ClipInfo(row[0], int(row[1]),
                         int(row[2]), row[3], row[4:]))

    process_videos(clips)
