import ffmpeg
import sys


def genvid(instream: str, output: str, start: int, end: int, options: dict = None):
    if (options == None):
        options = {}

    instream = ffmpeg.input(instream, ss=start, to=end)

    audio = fade_ffmpeg_audio_stream(
        instream.audio, start, end - start, options)
    video = fade_ffmpeg_video_stream(
        instream.video, start, end - start, options)

    proc = ffmpeg.output(video, audio, output)

    ffmpeg.run(proc)


def fade_ffmpeg_audio_stream(audio, start: int, end: int, options: dict = None):
    if (options == None):
        options = {}

    if ('fade_duration' not in options):
        options['fade_duration'] = 3

    audio = audio.filter('afade', t='in', st=0,
                         d=options['fade_duration'])
    audio = audio.filter('afade', t='out', st=end -
                         options['fade_duration'], d=options['fade_duration'])
    return (audio)


def fade_ffmpeg_video_stream(video, start: int, end: int, options: dict = None):
    if (options == None):
        options = {}

    if ('fade_duration' not in options):
        options['fade_duration'] = 3

    video = video.filter('fade', t='in', st=0,
                         d=options['fade_duration'])
    video = video.filter('fade', t='out', st=end -
                         options['fade_duration'], d=options['fade_duration'])
    return (video)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: gen_feded_video_with_text.py <input> <output> <start> <end>")
        sys.exit(1)
    genvid(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
