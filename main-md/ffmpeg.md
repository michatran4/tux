# ffmpeg
![](../img/FFmpeg.png)
ffmpeg is a powerful suite of programs and libraries for converting and
processing video and audio files.

## Usage
- ffmpeg [options] -i input output

## Options
ffmpeg requires an input file and an output file name.

Without any options, ffmpeg also automatically applies its own compression and
it can convert between file formats based on the input and output's extensions.

- **-i** location of the input file on the system
- **-ss** beginning timestamp to process media, default is the beginning of the
file
- **-to** ending timestamp to process media, default is the end of the file
- **-t** how much time, in seconds, of the media to process
- **-loop** usually for making gifs; loop the file
- **-map_metadata -1** Strip metadata.
- **-c:v copy** copy video stream
- **-c:a copy** copy audio stream

## Source code
ffmpeg is in development. You can view its source code
[here.](https://git.ffmpeg.org/ffmpeg.git)

*Page added on 2021-09-16, last edited on: 2021-12-10*

