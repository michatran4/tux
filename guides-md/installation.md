# General Linux installation
These general pointers are for linux installations.

## Pre installation
Rufus/balenaEtcher can be used to flash an ISO image to a USB drive.

## During installation
btrfs is a very good filesystem.

- One must format the partitions after allocating space for them.

## Post installation
### Adding users
- Use `visudo` if editing the sudoers file. Follow the template:

        root ALL=(ALL) ALL

### Window managers
Window managers are a minimalist alternative to desktop environments.
They typically operate with keybinds.

- Install a window manager, terminal emulator, and file manager.
- One may want a display manager or status bar.
- I use a clipboard manager, clipit.

### Moving /home
You may want to move /home after installation of a system to a partition with
more space. These commands need root permission.

Use the appropriate filesystem type and partition name.

- Create a new partition, format it, and mount it to **/mnt**.

- `cp -rp /home/* /mnt`
- `cd /`
- `mv /home /home.orig`
- `mkdir /home`
- `umount /dev/partition`
- `mount /dev/partition /home`
- `cp /etc/fstab /etc/fstab.orig`
- `chmod a=rwx /etc/fstab`
- Edit fstab to look like the following, using tabs:

        /dev/partition  /home   btrfs   defaults        0       0

- Optionally, delete **home.orig** after checking `df /dev/partition`.

## NVIDIA Drivers
NVIDIA doesn't play well with Linux. If you use NVIDIA graphics, you will need
to install appropriate drivers for optimal display functionality, like turning
up the refresh rate.

*Page added on 2021-11-10*

