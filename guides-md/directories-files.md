# Linux Directories and Files
Linux differs greatly from an operating system like Microsoft Windows regarding
how it manages its files and permissions.

## Directories
Linux directories can be separated into root's directories and a normal user's
directories. Each directory has a unique purpose.

## Root
- **/bin** contains essential binaries.
- **/boot** contains static boot files.
- **/dev** has files that represent drives on the system.
- **/etc** has global configuration files.
- **/home** contains home folders for all the users.
- **/lib** contains essential libraries.
- **/lost+found** contains lost and found files from corruption.
- **/media** is used for mounting removable devices.
- **/mnt** is used as a temporary mount point.
- **/proc** has files that represent system and process information.
- **/root** is root's home directory.
- **/tmp** is for temporary files.
- **/usr** is for non-essential, user binaries.
- **/var** has log files.

## User
- **~** is the user's home directory.
- **~/.config** is for local configuration files.
- **~/.local/bin** is for local executables.
- **~/.local/share** is for user data.

## Files
Files have permissions on them. By default, a file creator owns the file, and if
the root user owns a file, then a normal user will have to gain access to it
before reading/writing/executing.

[chown](../fileman/chown.html) can be used to change file ownership, and
[chmod](../fileman/chmod.html) can be used to change file permissions.

Symbolic links can act as shortcuts and they act as pointers to files.

*Page added on 2021-10-27, last edited on: 2021-12-10*

