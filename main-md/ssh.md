# ssh
ssh is used to remotely login to other computers and execute commands.

## Usage
- ssh [options] [destination] [command]

## Options
- **-p** Specify the port to connect to.
- **-q** Quiet mode.
- **-X** Enables X11 forwarding.

## Key-based SSH
Use public key authentication instead of just passwords.
- Generate public and private SSH keys on the client.
    - If it doesn't already exist, <code>mkdir ~/.ssh</code>
    - <code>ssh-keygen -t rsa -b 4096</code>
    - Public key: ~/.ssh/id_rsa.pub
    - Private key: ~/.ssh/id_rsa
    
- Transfer the public key.
    - If the host is currently using password authentication, <code>ssh-copy-id user@host</code>
    - Else, copy the public key file to the host and add it manually to ~/.ssh/authorized_keys

*Command added on 2021-10-18*

---

[homepage](../index.html)\
All site content is in the [Public Domain](http://unlicense.org/).
