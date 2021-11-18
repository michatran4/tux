# pass
pass stores, receives, generates, and synchronizes passwords.

## Usage
- pass [options]

## Options
With no options, pass prints out the existing passwords.
    
- **init "key"** Initialize a password store; should be done with your [GPG key.](./gpg.html)
- **insert [name]** Insert a password with standard input.
- **edit [name]** Edits a password. 
- **generate [-n] [-c] [name] [length]** Generates a password.
    - **-n** restricts special symbols.
    - **-c** copies the password instead of printing.
- **rm [name]** Removes the password.
- **show [-c] [name]** Shows the password. -c copies the password instead of printing.

*Page added on 2021-10-14*

---

[homepage](../index.html)\
All site content is in the [Public Domain](http://unlicense.org/).
