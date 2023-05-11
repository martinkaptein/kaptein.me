---
title: "Ubuntu Touch on the LG Nexus 4 in 2018 - the painful installation and review"
date: 2018-04-09
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - smartphone
  - mobile
  - ubports
  - ubuntu touch
  - linux
  - nexus 4
slug: ubuntu-touch-on-nexus-4-in-2018-installation-and-review
comments: true
description: "Review and installation of Ubuntu Touch UBports on the LG Nexus 4 in 2018. My opinion and experience with Ubuntu Touch and tutorial for installation. Trouble installaing Ubuntu Touch operating system on Nexus 4."
authors: ["martinkaptein"]
cat:
  - technology
---

As I have already stated in my [previous blog post about using a LG Nexus 4 in 2018](../using-a-nexus-4-in-2018/) I am a big fan of Ubuntu Touch (ubports) on the Nexus 4, and one of the view (conceptually-) new operating system, in the development of which, I, indeed, believe.

In this blog entry, I will report about my troubles of installing Ubuntu Touch operating system (using the GUI installer) on the Nexus 4, providing a tutorial about the solutions which helped me (and might as well help you).

Then, I will review the Ubuntu Touch operating system, and tell my opinion about it.

## Installing Ubuntu Touch on the Nexus 4 

The installation of Ubuntu Touch operating system (ubports) on the Nexus 4 is truly a pain, even though there is a very nice installer which (in theory) should work just fine.

I tried the installer, in all operating systems, for me it failed in Windows and MacOS. 

### Virtual Box
What finally saved me was a Ubuntu Installation in Virtual Box.
However, that also didn’t work directly. Please make sure to install the [Virtual Box extension pack](https://www.virtualbox.org/wiki/Downloads), then in the settings for the Virtual Machine enable at least the USB 2.0 controller (this option is only available when you install the VB extension pack.

Then, also in the Virtual Machine settings make sure to add the USB device filters and *NOTE:* add both the filter for the device in fast boot mode as well as in recovery mode (those are different USB addresses).

It should look something like this:

![Virtual Box USB settings screenshot](/images/blog/vb-screenshot.jpg)

*Virtual Box USB settings screenshot*

Then, inside Ubuntu (I mean the desktop system now), download and install the UBports installer ([download here](https://github.com/ubports/ubports-installer/releases/latest)).

Installation can be done with:

`sudo dpkg -i filename.deb`

and (if there are errors)

`sudo apt-get install -f`

After that, please make sure to add the dev rules (as seen on [the UBports Github page here](https://github.com/ubports/ubports-installer/tree/0.1.11-beta#how-to-install) (make sure to scroll down)).

Of course for that udev has to be installed (=`sudo apt-get install udev`).

Then, check if `/etc/udev/rules.d/51-android.rules` exists (if not create it with `sudo touch /etc/udev/rules.d/51-android.rules`) and add the following lines to it (for example using `nano` or `gedit`):

```

SUBSYSTEM=="usb", ATTRS{idVendor}=="0bb4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="0e79", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0502", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0b05", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="413c", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0489", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="091e", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="18d1", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0bb4", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="12d1", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="24e3", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="2116", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0482", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="17ef", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="1004", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="22b8", MODE="0666", GROUP="plugdev"    
SUBSYSTEM=="usb", ATTRS{idVendor}=="0409", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="2080", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0955", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="2257", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="10a9", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="1d4d", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0471", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="04da", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="05c6", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="1f53", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="04e8", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="04dd", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0fce", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="0930", MODE="0666", GROUP="plugdev"  
SUBSYSTEM=="usb", ATTRS{idVendor}=="19d2", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTRS{idVendor}=="2ae5", MODE="0666", GROUP="plugdev"

```

And restart udev service with `sudo service udev restart`.

Again, this tutorial comes from [here](https://github.com/ubports/ubports-installer/tree/0.1.11-beta#how-to-install).

Restart whole system, just to make sure.

After that run the GUI installer. 

For me device auto-detection didn’t work, I selected Nexus 4 manually, then connected it while in fastboot.

Also, last but not least if there are any errors (or hangups) during the installation process a `adb kill-server` and then `adb start-server`should solve the problems.

I wish you good luck with the installation, it is quite a challenge (although for many people it appears to work just fine).

## Ubuntu Touch on Nexus 4 review

The system itself works just splendid, I didn’t encounter any bugs. Battery life is also great, especially standby time.

The design is very intuitive (especially the swiping from the edges). After a day, I found myself doing the same on my main phone.

The Appstore situation if quite sad still, although there are continuously new apps added. There is even offline GPS navigation software.

![ubuntu touch open store](/images/blog/ubports-open-store.jpg)

*ubuntu touch open store on Nexus 4*.

Only app I didn’t discover was a mail-client (if you are into that sort of things).

Overall, I like the design a lot. The browser also seems to support all the modern web-techonolgies (which is important for a system with limited set of apps).

![Ubuntu Touch lockscreen](/images/blog/ubports-lockscreen.jpg)

*Ubuntu Touch lockscreen*

![Ubuntu Touch notification tray](/images/blog/ubports-notification.jpg)

*Ubuntu Touch notification tray*

![Ubuntu Touch multitask interface](/images/blog/ubports-multitask.jpg)

*Ubuntu Touch multitask interface*


Also, the terminal app, is the best default Terminal app, I have yet seen on a mobile system.

![Ubuntu Touch terminal](/images/blog/ubports-terminal.jpg)

*Ubuntu Touch terminal*

Root access is no problem (your device password is use for root access), SSH and ADB shell access is no problem either.

Anyway, there is still a lot to be said about this system.

The Nexus 4 will very likely receive the next Ubuntu Long Term Support update, which (from what I understand) should come with Anbox, which will allow to run Android apps on Ubuntu Touch.

Packet managers don’t work (obviously - due to architecture stuff), though it would be nice to see `apt-get` or `snap` on Ubuntu Touch.

Anyway, the system is very developer friendly, and what I really like is, that it can be easily transformed into a Desktop operating system (which it basically is).

## Verdict

A great system, with a thriving developer community, and a future. I do really believe in it.
