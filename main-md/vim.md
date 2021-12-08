# vim
![](../img/vim.png)

*Image by [User:D0ktorz](https://commons.wikimedia.org/wiki/User:D0ktorz) - [Image](https://commons.wikimedia.org/wiki/File:Vimlogo.png) reworked in SVG, [GPL](http://www.gnu.org/licenses/gpl.html), [Link](https://commons.wikimedia.org/w/index.php?curid=1228427)*

vim is a text editor.

## Usage
- vim [file(s)]

## Options
- **-n** Don't use a swap file.
- **-R** Read-only mode.
- **-x** Encrypt written files.

## Examples
vim is a keyboard centric program.

### Basics
- **i** Go into insert mode (left of the cursor).
- **ESC** Return to command mode.
- **h** Move left one character
- **j** Move down one line
- **k** Move up one line
- **l** Move right one character
- **w** Move forward to the beginning of the next word
- **e** Move forward to the end of the next word
- **b** Move back one word
- **/** Search
- **n** Next item in search
- **N** Previous item in search
- **p** Paste after cursor
- **x** Delete one character
- **y** Yank/copy
- **Y** Yank line
- **u** Undo
- **^r** Redo
- **v** Visual mode
- **V** Visual line mode
- **^v** Visual column mode
- **:[number]** Go to a line number.
- **:w** Write
- **:wq** Write and quit
- **:q** Quit
- **:q!** Force quit

### More editing
- **a** Go into insert mode to the right of the cursor.
- **A** Go into insert mode at the end of the line.
- **I** Go into insert mode at the first non-whitespace character.
- **J** Join the current line with the next line.
- **o** Make a new line below the current line and go into insert mode.
- **O** Make a new line above the current line and go into insert mode.
- **s** Change the current character.
- **S, cc** Change the current line.
- **>** Indent
- **<** Unindent

### More moving
- **W** Move forward one Word (beginning)
- **E** Move forward one Word (end)
- **B** Move back one Word
- **0** Go to the beginning of the line.
- **$** Go to the end of the line.
- **gg** Go to the beginning of the file.
- **G** Go to the end of the file.
- **t[char]** Go to the next occurrence of char.
- **T[char]** Go to the previous occurrence of char.
- **{** Go to the previous section, separated by newlines.
- **}** Go to the next section, separated by newlines.

### Change/Delete
The change (c) and delete (d) commands can be used as a prefix for other binds.

- **[prefix]w** Operate on the word at the cursor
- **[prefix]t[char]** Operate from the cursor to the next occurrence of char.
- **[prefix]T[char]** Operate from the cursor to the previous occurrence of
char.
- **[PREFIX]** Operate to the end of a line.

### Miscellaneous
- **~** Toggle case of a character.
- **gq** Format a visual section to the correct number of characters per line.
- **:[command]** Execute a command.

## Source code
vim is in development. You can view its source code
[here.](https://github.com/vim/vim)

neovim, a fork of vim, is also in development. You can view its source code
[here.](https://github.com/neovim/neovim)

*Page added on 2021-10-15*

