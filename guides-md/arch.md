# Arch Linux
Arch Linux has been my daily driver for the past two years of using Linux.

## Installation guide supplement
- A wireless network can be connected to using `wpa_supplicant`.
    - 1's i's and L's may look very similar when inputting an SSID.
- cfdisk can be used to partition disks graphically.
    - M stands for MB and G stands for GB.
    - Remember to have an EFI partition if necessary. EFIs have the type 'EFI
    system' and roots have the type 'Linux filesystem.'
- Install networkmanager with pacstrap for networking.
- Install efibootmgr and os-prober for multiple operating systems.
- Install vim or nano for text editing.

## pacman
### Options
- **-Syu** synchronizes repository databases and updates all packages
- **-S [package(s)]** install packages
    - Repositories must be defined if multiple versions are present in different
    ones.
- **-R [package(s)]** remove packages, leaving dependencies installed
- **-Rs [package(s)]** remove packages, uninstalling dependencies not required
by other packages
- **-Rsc [package(s)]** remove packages recursively, uninstalling dependencies
and packages using those dependencies
- **-Rn** add the n option to any of the previous remove commands to also remove
important configuration backup files
- **-Ss [string(s)]** search for an uninstalled package
- **-Qs [string(s)]** search for installed packages
- **-Qdt** list orphans

### Other
pacman can ignore packages in **/etc/pacman.conf**, specified by the **IgnorePkg** line.

Install an AUR helper, like `yay`, to help with the AUR. Options are the same as
pacman.

- `git clone https://aur.archlinux.org/yay.git`
- `cd yay`
- `makepkg -si`
- `cd ..`
- `rm -rf yay`

## Miscellaneous
- xdg-settings can set default applications if the desktop environment doesn't have an option for it.

Example:

    xdg-settings set default-web-browser brave.desktop

*Page added on 2021-11-10*

