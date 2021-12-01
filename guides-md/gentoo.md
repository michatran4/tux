# Gentoo Linux
Gentoo is one of the most tedious operating systems I have ever used.

## Installation
- Revise **/etc/portage/make.conf**.

https://gist.githubusercontent.com/michatran4/58e7ccb539156d69b6519d303e66b3d9/raw/c923fd3d3d5ec695deb27062c24af547346b6dd2/make.conf

These options should be customized according to one's hardware. I used NVIDIA
graphics with Gentoo.

- Update mirrors, using mirrorselect.

`mirrorselect -i -o >> /mnt/gentoo/etc/portage/make.conf`

- Emerge **rust-bin** before running `emerge --sync`.
- Install ccache.
- I accept every package license in **/etc/portage/package.license**.

## NVIDIA with Gentoo
- Add **blacklist nouveau** to **/etc/modprobe.d/blacklist.conf** before
emerging **nvidia-drivers**.
- If using genkernel, one must always install compatible nvidia drivers after
compiling a new kernel.

## dwm autostart
I use xrandr to fix my display orientations.

## Miscellaneous
**/etc/mime.types** can be edited to rearrange extension priorities.

*Page added on 2021-11-09*

