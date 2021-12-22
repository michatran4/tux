# rsync
rsync allows you to remotely sync files between computers.

It can also be used to sync contents between two directories.

## Usage
- rsync [options] [source] [destination]

## Options
By default, rsync is not recursive.
- **-r** recursively sync, used for directories
- **-a** archive; sync recursively and preserve all file properties
- **-v** toggle verbosity

## Examples
- **rsync -a ~/dir1 user@host:dir2** sync a local directory/file to a remote server
- **rsync -a user@host:/home/user/dir1 dir2** sync a remote directory/file locally
- **rsync -ae 'ssh -p [1024]' [source] [dest]** sync, but provide a
different port number as the machine uses a non default ssh port.

*Page added on 2021-11-12, last edited on: 2021-12-08*

