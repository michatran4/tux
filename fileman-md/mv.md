# mv
mv moves/renames files.

## Usage
- mv [options] [source(s)] [directory]

## Options
- **-b** make a backup of each existing destination file
- **-f** do not ask before overwriting
- **-i** prompt before overwrite
- **-n** do not overwrite an existing file

If you specify more than one of -i, -f, or -n, only the final one takes effect.

- **-t** move *sources* to *directory*
- **-u** only move when the source file is newer than the destination file, or
if the destination file does not exist
- **-v** toggle verbosity

*Page added on 2021-10-01, last edited on: 2021-12-08*

