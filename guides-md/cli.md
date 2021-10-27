# CLI Quirks
The command line interface usually has some general features to aid the average user.
It is considered to be much more versatile than a graphical interface.

## -h and -v
Commands usually have a -h and a -v option. -h displays the help for the command, and -v displays the version of the utility.

## Linux Control Operators
- **;** indicates separate commands.
- **&** indicates the line preceding it is run in the background.
- **&&** is the AND operator. It runs the second command if the first command does not fail. It has higher precedence than the OR operator.
- **||** is the OR operator. It runs the second command if the first command fails.
- **#** indicates a comment, ignored by the shell.
- **\\** escapes control characters, and can be used to indicate a new line if used at the end.

## Piping
Commands can be used in conjunction with other commands. An example is lolcat, which can read text and output it with different colors.

<code>cat file | lolcat</code>

## Output management
The greater than symbol can be used to redirect output.
- \> overwrites the file.
- \>> appends the output to the file.

## Shebangs
#! followed by a path makes the shell use the specified interpreter, when the file is used as an executable.
- **#!/bin/sh** uses a POSIX compliant shell.
- **#!/bin/bash** uses the bash shell.
- **#!/usr/bin/env python3** uses a Python interpreter.

*Command added on 2021-10-25, last edited on 2021-10-27*

---

[homepage](../index.html)\
All site content is in the [Public Domain](http://unlicense.org/).
