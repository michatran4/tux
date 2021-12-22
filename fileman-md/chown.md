# chown
chown changes the file owner and group.

## Usage
- chown [options] [owner][:[group]] [file]

## Options
By default, symbolic links are not traversed recursively, and the referent of
the links are affected by chown.

- **-c** Like the verbose option, but only state changes
- **-f** Suppress most error messages
- **-h** Change the ownership of symbolic links instead of the referenced file
- **-v** List every file operation
- **-R** Change file permissions recursively

*Page added on 2021-09-30*

