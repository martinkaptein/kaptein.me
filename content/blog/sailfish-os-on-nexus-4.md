---
title: "Installing Sailfish OS on Google Nexus 4"
date: 2018-03-10
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - smartphone
  - mobile
  - Sailfish OS
  - LG Nexus 4
  - Tutorial
slug: sailfish-os-on-nexus-4
comments: true
description: "In this tutorial I will show how to install Sailfish OS on a LG Nexus 4."
authors: ["martinkaptein"]
cat:
  - technology
---


In this tutorial I will show how to install Sailfish OS on a LG Nexus 4.
This post assumes that:

- You are rooted
- You have a custom recovery (I had the latest TWRP recovery)
- You have adb, fast boot and device drivers installed on your PC.
- You have a very basic understanding how this stuff works
- You made backups (since you will lose all data)
- If you brick your device I am not responsible

Without further a do, here we go!



## Installing Sailfish OS
 
This tutorial will show the simplest way to install Sailfish OS on a Nexus 4. So stuff like Multirom aren’t necessary.
First of all, download the latest Sailfish OS port [here](http://images.devaamo.fi/sfe/mako/gamma8/sailfishos-mako-release-2.0.5.6-gamma8.zip). 


Then download CyanogenMod [here](http://cyanogenmod.org.ru/arh/cm-11-20141115-SNAPSHOT-M12-mako.zip).
If the links don’t work, feel free to [contact](/contact/) me, I will upload this stuff to Dropbox or something.

After that, transfer the files to your device, using any method you are comfortable with (for example `adb push`).

Now, boot your device to recovery, install first the CyanogenMod zip (*flash zip*), and directly after that (without restarting) the Sailfishos zip. Then restart your device.

![installing the zips](/images/installing_zip_sailfishos.jpg)

*installing the zip files*

Sailfish OS should boot just fine.

It should be noted, that not all of the stuff worked for me (for example Bluetooth).

For more information you should see the [official site of the Sailfish OS port for the Nexus 4 here](https://wiki.merproject.org/wiki/Adaptations/libhybris/Install_SailfishOS_for_mako).

### Sailfish OS on Nexus 4 in action.

![Sailfish OS on Nexus 4 in action 1](/images/sailfish-os-in-action-1.jpg)

![Sailfish OS on Nexus 4 in action 2](/images/sailfish-os-in-action-2.jpg)

*Sailfish OS on Nexus 4 in action*


## Conclusion

This is a very nice way, to get a glimpse at Sailfish OS, without buying a dedicated phone (which are, right now, quite hard to find).
