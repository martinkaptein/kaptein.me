---
title: "Arch Linux Offline Installation"
date: 2022-07-29T15:58:50+02:00
draft: false
# write a good description
description: "Installing Arch Linux without an internet connection from just a USB drive. No caching of Pacman repositories required. This method basically copies the Arch Linux filesystem from the USB drive to the computer."
# meta image relative to this file
#Set to true to have Table of Content
# cat = {tag&category}
cat:
  - linux
  - technology
---


Recently I have switched to [Arch Linux](https://archlinux.org/).
The manual installation is quite straightforward following the Arch Linux Wiki, but I wondered how an Arch Installation would be possible from just a USB drive, without an internet connection and without any caching of Pacman/Pacstrap programs and repositories.
The goal is to have the same working system, which you would normally have booted from a USB drive, but installed to your hard drive.
The sporting challenge commences..

## Assumptions

This *tutorial* assumes that you have a USB drive with Arch prepared and booted up.
At the moment of writing it is version `2022.07.01`.
Moreover, I will be covering a BIOS MBR installation (so **no UEFI**), as it is a little bit more simple.
On most BIOS'es you can still switch to BIOS boot mode (often referred to as legacy boot), if you should wish so.

## Offline installation from USB drive

Assuming you have booted from the USB drive, first thing to do is the partitioning:

## Partitioning

Let's assume you have the most simple partition layout, a **SWAP** partition (for more RAM and possibility for hibernation) and a **root partition** for the root file system.
Strictly speaking for BIOS MBR boot you don't need more partitions than these two.

However, usually the convention is to add a boot and home partition too.
For the sake of this article we will skip that though.

In my case I created a SWAP partition with double the amount of RAM and used the rest of the space for the root filesystem.
You can use `fdisk /dev/sda` for the partitioning, assuming that your main hard drive is `/dev/sda` (use `lsblk` to find that out).
See the [Arch Wiki Installation Guide](https://wiki.archlinux.org/title/Installation_guide), if you need more guidance with any of those steps.

Assuming that `/dev/sda1` will be SWAP and `/dev/sda2` root you can format the partitions now:

```
mkswap /dev/sda1
swapon /dev/sda1
mkfs.ext4 /dev/sda2
```

Mount the root partition so we can copy the Arch Linux installation to it from the USB drive:

```
mount /dev/sda2 /mnt
```

## Copying files to root system

At the time of writing, on the Arch Wiki there is a page about [offline Arch Installation](https://wiki.archlinux.org/title/Offline_installation) but I found that some parts weren't exactly functional.

Instead of `cp` I used `rsync` to copy the files over:

```
rsync -avl /{bin,boot,etc,home,lib,lib64,opt,root,sbin,srv,sys,usr,var} /mnt
```

This step will take quite a long time.
Note that we don't want to copy all the files from the Linux filesystem.

Next, copy the kernel image in the same way (Arch places it on the live ISO in a different location than usual):

```
rsync -avl /run/archiso/bootmnt/arch/boot/x86_64/vmlinuz-linux /mnt/boot/
```

Generate the fstab:

```
genfstab -U /mnt >> /mnt/etc/fstab
```

Now you should be able to chroot into the Arch Linux installation on your hard drive:

```
arch-chroot /mnt
```

If this gives an error, you will have to re-create the directories it complains about, e.g.:

```
mkdir /mnt/{dev,proc,run,tmp}
```

### Config

Now you can do the basic usual configuration, as is described on the Arch Wiki.
Set the hostname, locale, timezone, hostname, set root passwd, create other users etc..

Import the archlinux keys:

```
pacman-key --init
pacman-key --populate
```

A point of attention is the mkinitcpio conf file in `/etc/mkinitcpio.conf`.
Remove there the hooks you don't need so you will just have:

```
HOOKS=(base udev autodetect modconf block filesystems keyboard fsck)
```

Initramfs:

```
mkinitcpio -P
```

### Bootloader 

A very important step is to install the bootloader, otherwise your system will not start.
In this case I went with GRUB.

```
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```

Now you can exit the chroot environment and reboot.
You should have the full Arch Linux ISO installed on your hard drive, with all the tools it came with, without any internet connection!

By the way, you can also [encrypt an offline Arch Linux setup](/blog/arch-linux-encrypted-full-install/).
