# cp
cp copies files from all directories up to the last directory, to the last directory.

## Usage
- cp [options] [source(s)] [directory]

## Options
By default, cp does not copy recursively.
- **-i** Prompts before overwriting a file
- **-n** Do not overwrite any existing files (overrides a previous -i option)
- **-p** Preserve attributes
- **--no-preserve=ATTR_LIST** Don't preserve specified attributes
- **-r** Copy directories recursively
- **-s** Make symbolic links instead of copying
- **-t** Copy *sources* to *directory*
- **-u** Only copy when the source file is newer than the destination file, or if the destination file does not exist
- **-v** List every file operation

*Page added on 2021-09-30*

---

[homepage](../index.html)\
All site content is in the [Public Domain](http://unlicense.org/).
