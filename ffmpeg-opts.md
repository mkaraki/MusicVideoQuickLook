# ffmpeg options
This is just a note for developpers.

## Cut
```shell
$ ffmpeg -i foo.mp4 -ss $START_SEC -t $CUT_DURATION -c copy bar.mp4
```

```shell
$ ffmpeg -i foo.mp4 -ss $START_SEC -to $END_SEC -c copy bar.mp4
```

## Audio Fade in/out
```shell
$ ffmpeg -i foo.mp4 -v:c copy -af "afade=t=in:st=$START_SEC:d=$FADE_DURATION,afade=t=out:st=$END_SEC:d=$FADE_DURATION"
```

## Video Fade in/out
```shell
$ ffmpeg -i foo.mp4 -a:c copy -vf "fade=t=in:st=$START_SEC:d=$FADE_DURATION,fade=t=out:st=$END_SEC:d=$FADE_DURATION"
```