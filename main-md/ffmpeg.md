# ffmpeg
![](../img/FFmpeg.png)
ffmpeg is a powerful suite of programs and libraries for converting and processing video and audio files.

## Usage
- ffmpeg [options] -i input output

## Options
ffmpeg requires an input file and an output file name. ffmpeg also automatically applies its own compression, so you could just pass it a file with the -i flag and it will try its best to compress the file.

- **-i** Location of the input file on the system
- **-ss** Beginning timestamp to process media, default is the beginning of the file
- **-to** Ending timestamp to process media, default is the end of the file
- **-t** How much time, in seconds, of the media to process
- **-loop** Usually for making gifs; loop the file
- **-map_metadata -1** Strip metadata.

## Source code
ffmpeg is in development. You can view its source code [here.](https://git.ffmpeg.org/ffmpeg.git)

*Page added on 2021-09-16, last edited on: 2021-10-19*

