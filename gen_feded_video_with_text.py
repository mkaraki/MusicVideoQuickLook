import ffmpeg
import sys
import gen_feded_video


def gentxtvid(instream, output, start, end, title, infos=[], options={}):
    if ('font' not in options):
        options['font'] = ''
    if ('bgcolor' not in options):
        options['bgcolor'] = 'black@0.4'
    if ('fgcolor' not in options):
        options['fgcolor'] = 'white'
    if ('infotime' not in options):
        options['infotime'] = 8

    instream = ffmpeg.input(instream, ss=start, to=end)
    video = instream.video

    # Write BG Box
    video = video.drawbox(x=0, y='ih-150', width='iw', height=150,
                          color=options['bgcolor'], thickness='fill')

    # Write Title
    video = video.drawtext(text=title, x=25, y='h-130',
                           fontfile=options['font'], fontsize=64, fontcolor=options['fgcolor'])

    # Write infos
    for i in range(0, len(infos) - 1):
        video = video.drawtext(text=infos[i], x=25, y='h-55',
                               fontfile=options['font'], fontsize=32, fontcolor=options['fgcolor'],
                               enable='between(t,' + str(i*options['infotime']) + ',' + str((i+1)*options['infotime']) + ')')

    # Write last information (for inf duration)
    video = video.drawtext(text=infos[-1], x=25, y='h-55',
                           fontfile=options['font'], fontsize=32, fontcolor=options['fgcolor'],
                           enable='between(t,' + str((len(infos) - 1)*options['infotime']) + ',' + str(end - start) + ')')

    # Fade in/out
    video = gen_feded_video.fade_ffmpeg_video_stream(
        video, start, end - start, options)
    audio = gen_feded_video.fade_ffmpeg_audio_stream(
        instream.audio, start, end - start, options)

    if ('return_stream' in options and options['return_stream']):
        return (video, audio)

    # Save
    proc = ffmpeg.output(video, audio, output)

    # Exec
    ffmpeg.run(proc)


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: gen_feded_video_with_text.py <input> <output> <start> <end> <title/artist> <information>...")
        sys.exit(1)
    gentxtvid(sys.argv[1], sys.argv[2], int(sys.argv[3]),
              int(sys.argv[4]), sys.argv[5], sys.argv[6:])
    exit
