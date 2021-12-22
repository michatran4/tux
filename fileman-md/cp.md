# cp
cp copies files.

## Usage
- cp [options] [source(s)] [destination]

## Options
By default, cp does not copy recursively.

- **-i** prompts before overwriting a file
- **-n** do not overwrite any existing files (overrides a previous -i option)
- **-p** preserve attributes
- **--no-preserve=ATTR_LIST** don't preserve specified attributes
- **-r** copy directories recursively
- **-s** make symbolic links instead of copying
- **-t** copy *sources* to *directory*
- **-u** "update", only copy when the source file is newer than the destination file, or
if the destination file does not exist
- **-v** toggle verbosity

*Page added on 2021-09-30, last edited on: 2021-12-08*

