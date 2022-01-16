import ffmpeg
import sys
import process


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: process_and_combine.py <input csv> <output>")
        sys.exit(1)

    clips = process.get_clips_from_csv(sys.argv[1])

    streams = process.process_videos(clips, {'return_stream': True})

    concat = ffmpeg.concat(*streams, v=1, a=1)
    output = concat.output(sys.argv[2])
    output.run()
