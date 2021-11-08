# Linux Distributions
Linux distributions/distros have varying purposes and traits that set them apart
from one another. Their main difference is how they manage packages.

Stable distributions are usually considered stable because of their older,
tested, and reliable packages. These distributions usually have derivatives
that are more fitting for the average computer user.

Testing/rolling release/unstable distributions are considered to be
'bleeding-edge' because they have fresh packages. 

## Daily drivers
Daily driver distributions come ready to use out of the box.

- Ubuntu
    - Type: Stable
    - Parent distro: Debian
    - Default DE: GNOME
    - Other flavors: Xubuntu, Kubuntu, Lubuntu, Ubuntu MATE, Ubuntu Budgie
    - Package manager: apt

- Linux Mint
    - Type: Stable
    - Parent distro: Ubuntu LTS
    - Default DE: Cinnamon
    - Other flavors: MATE, XFCE
    - Package manager: apt

- Fedora
    - Type: Stable
    - Parent distro: N/A
    - Default DE: GNOME
    - Other flavors: Cinnamon, i3, KDE, LXDE, LXQt, MATE, XFCE
    - Package manager: dnf

- openSUSE
    - Type: Rolling release (Tumbleweed), Stable (Leap)
    - Parent distro: N/A
    - Default DE: KDE
    - Other flavors: GNOME, XFCE, LXDE, +
    - Package manager: zypper

- EndeavourOS
    - Type: Rolling release
    - Parent distro: Arch
    - Default DE: XFCE
    - Other flavors: Budgie, Cinnamon, GNOME, i3, KDE, LXQt, MATE
    - Package manager: pacman

- Garuda Linux
    - Type: Rolling release
    - Parent distro: Arch
    - Default DE: KDE
    - Other flavors: bspwm, GNOME, i3, KDE, LXQt, MATE, Qtile, Sway, Wayfire,
    XFCE
    - Package manager: pacman

## Stable distros
- Debian

Debian is a parent distribution of many, like Ubuntu and Linux Mint. It is used
on both desktop and servers. By default, Debian comes with the GNOME desktop
environment.

- Devuan

Devuan is a fork of Debian without systemd.

## Power user distros
Power user distributions have unique purposes for power users.
- Arch

Arch is a binary based distribution. It has a few solid derivatives: Garuda,
EndeavourOS, Artix, and Blackarch. Arch is very hands on and bare bones, meaning
it comes out of the box with barely anything for daily usage. By default, this
forces the user to customize it.

- Gentoo

Due to Gentoo's nature as a source based distribution, all software should be
compiled from source on the system, tailored to ones' hardware and needs with
configuration files. The length of the installation period depends on the speed
of one's hardware and specified USE flags. Maintenance requires consistent
compiling and updating.

- Void Linux

Void Linux's xbps package manager allows one to install software distributed in
binaries or build from source.

- Alpine Linux

Alpine Linux is a lightweight and security-oriented distribution that does not
use the GNU coreutils.

- NixOS

NixOS was designed to have reproducible builds across all systems.
The entire operating system is built by the package manager from a configuration
file.

## Miscellaneous distros
- Kali

Kali is used for penetration testing. It is not recommended to be used as a
daily driver.

- BlackArch

BlackArch is also a operating system for penetration testing.

- Tails OS

Tails routes all connections through the Tor network.

- Puppy Linux

Puppy Linux is a family of Linux distributions that are extremely lightweight.
It contains options from Ubuntu, Raspbian, and Slackware.

## Distros to avoid
- Manjaro

Manjaro is a poor derivative of Arch Linux. It claims to be a more stable
version of Arch by testing and holding back packages.
However, there is no point to this if the AUR exists, and many Arch users get
software from the AUR.

Manjaro's developers have asked its users to travel back in time when they
forgot to update their SSL certificates.

- Raspberry Pi OS

Raspberry Pi OS pings a Microsoft software repository when updating.

*Page added on 2021-11-08*

---

[homepage](../index.html)\
All site content is in the [Public Domain](http://unlicense.org/).
