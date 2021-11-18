# gpg
GnuPG allows you to encrypt and sign data.

## Usage
- gpg [options]

## Examples
- **gpg --full-generate** Generates a new GPG key. It defaults to using RSA with 2048 bits. Set it to be non expiring. The pass phrase is used to unlock the secret key.
- **gpg --list-secret-keys --keyid-format LONG** Fetch your public key under **sec rsa2048/*KEY***.
- **gpg -d [file.gpg]** Decrypt a .gpg file.

*Page added on 2021-10-14*

---

[homepage](../index.html)\
All site content is in the [Public Domain](http://unlicense.org/).
