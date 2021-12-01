# sudo
sudo allows for execution of commands as another user or the root user.

## Usage
- sudo [options] [command]

## Options
- **-U [user]** specify a user.

## Warnings
sudo recently suffered a vulnerability; privilege escalation was possible due
to a heap-based buffer overflow. An alternative to sudo is `doas`, or to just
switch to the root user for necessary operations. This warning is meant for
machines with more than one user.

*Page added on 2021-11-10*

