---
title: "Arch Linux Encrypted Full Install"
date: 2022-07-30T15:07:34+02:00
draft: false
# write a good description
description: "Installing Arch Linux on a fully encrypted drive, including the boot partition. It is actually quite straightforward to install Arch Linux fully encrypted for a BIOS MBR bootloader installation. "
# cat = {tag&category&keyword}
cat:
  - technology
  - linux
---


In this post we are going to have a look at how to perform the standard Arch installation but encrypted.
As it turns out, this is actually quite straightforward and requires only some minor tweaks to *Initramfs* as well as the bootloader (we will use *GRUB*).
For most of the steps you can just follow the Arch Wiki.

## Prerequisites

In this guide I will assume:

1. A BIOS MBR Boot Scenario. 

Apparently it has its advantages over UEFI, as it is much more simple to setup.
You can switch in many BIOS'es back to BIOS boot (=legacy boot).

2. Simple partition layout:

Double RAM space for SWAP on `/dev/sda1` and the rest for the root partition `/dev/sda2`.
Separate partitions for booting are hence not required.
This way everything will be encrypted except for the SWAP partition.

## Following the Arch Installation

### Encrypt the partition

Follow the first steps of the [standard Arch installation on the Arch Wiki](https://wiki.archlinux.org/title/Installation_guide), paying extra attention to select the correct keyboard layout.
Setup an internet connection (or you can use [my guide for a full offline install](/blog/arch-offline-install/) which also works with encryption).
Update the system clock and partition the disks with `fdisk /dev/sda` or something else.
As my method will require to embed GRUB in between the partition space you will need to use a DOS partitioning scheme[^gpttodos].

For the rest of the guide I will assume that your root partition, which will contain everything (except SWAP of course), will be on `/dev/sda2`.
If you chose to have SWAP you can already use `mkswap /dev/sda1` and `swapon /dev/sda1`.
Now, before we create the *ext4* Linux Filesystem on `/dev/sda2` we will need to encrypt it first:

```
cryptsetup luksFormat --type luks1 /dev/sda2
```

This will prompt you for the encryption password, be careful, don't loose it.
`--type luks1` is necessary because our bootloader, **GRUB**, doesn't fully support LUKS2 yet.
Unlock the Luks partition, create the EXT4 Linux filesystem "inside" it and mount it:

```
cryptsetup open /dev/sda2 root
mkfs.ext4 /dev/mapper/root
mount /dev/mapper/root /mnt
```

We see that now we have to access our unlocked partition/filesystem through `/dev/mapper/root`.
Later this will become a point to not become confused about.

### Install Arch to the encrypted partition

Now you can continue following the wiki, normally.
Select the mirrors and install Arch with Pacstrap (or use the [rsync offline install method](/blog/arch-offline-install)).

My Pacstrap command usually looks like this:

```
pacstrap /mnt base base-devel linux linux-firmware iwd neovim systemd mkinitcpio grub
```

Adding `mkinitcpio grub` and some text editor is recommended.
We will need to rebuild Initramfs with *mkinitcpio* after installation again, to support encryption, as well as install GRUB, so you might just as well include these programs here.
I like to include `iwd` for my wireless needs too.

Before chrooting into the installation you can also generate the Fstab:

```
genfstab -U /mnt >> /mnt/etc/fstab
```

### Setting up Arch Linux 

`arch-chroot /mnt` into arch, set up Arch normally, set timezone, locales, hostnames, set users and root password.

Now, as an extra step we will need to generate a new *initramfs* again, in order to support encryption Hooks when booting up.
Edit `/etc/mkinitcpio.conf`, make sure the Hooks look like this:

```
HOOKS=(base udev autodetect keyboard keymap consolefont modconf block encrypt filesystems fsck)
```

Now run mkinitcpio:

```
mkinitcpio -P
```

#### Setting up GRUB for an encrypted boot partition

Now we just need to set up GRUB to boot from our fully encrypted system (because everything is located in `/dev/mapper`).
For this we will need to get our UUID.
Just to make clear: You will in this case need the UUID of `/dev/sda2` and **NOT** of `/dev/mapper/root`.
Use `blkid` to find out this UUID and note it somewhere.

With this we can edit our Grub config in `/etc/default/grub`.

Basically you only need to uncomment:

```
GRUB_ENABLE_CRYPTODISK=y
```

And importantly set:

```
GRUB_CMDLINE_LINUX_DEFAULT="cryptdevice=UUID=youruuid:root root=/dev/mapper/root"
```

Of course, substitute *youruuid* with the UUID you noted earlier.

Then install grub and make the grub config:

```
grub-install --target=i386-pc /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
```

Grub should be installed directly on the drive (`/dev/sda`) and NOT on the sub-partition (`/dev/sda2`).

After this you can exit the chroot environment and reboot.
Now you should have a fully encrypted Arch install.

Keep in mind that in this setup you will need to enter your password twice.
It is possible to remedy that, but this will be slightly more complicated, warranting a deeper exploration of this topic.

### Update: Encrypting SWAP space

As leaving memory of your RAM, which is stored and retrievable in the SWAP space is hugely not desirable, it is much recommended to encrypt the SWAP partition as well.
In this case you will need to decide if you need the hibernation feature or not.
If you do not need hibernation, the setup will be quite simple.
This is easiest to do after the full Arch Installation.

First, turn off the current SWAP, using `swapoff /dev/sda1`.
Open both `/etc/crypttab` and `/etc/fstab` in text editors next to each other.

Copy the UUID of the SWAP partition from `/etc/fstab` over to the `/dev/sdX#` in `/etc/crypttab`.
Of course you will need to uncomment that line too.
After this, change the `UUID=youruuid` in `/etc/fstab` to `/dev/mapper/swap`.
This is because *crypttab* will automatically mount the SWAP partition with the UUID to `/dev/mapper/swap` initializing it with a unique key on every boot.

Now you have encrypted SWAP as well.

[^gpttodos]: If you need to convert from GPT back to MBR/DOS (for which there actually are legitimate reasons), you will need to "destroy" GPT using `gdisk /dev/sda` > advanced > z (zap). For me it also helped to mark `/dev/sda2` as bootable from fdisk. Otherwise you will have a system which cannot boot.
