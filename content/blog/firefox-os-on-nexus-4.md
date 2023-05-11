---
title: "Installing Firefox OS on Google Nexus 4"
date: 2018-03-10
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - Nexus 4
  - Smartphone
  - Firefox OS
  - Boot to Gecko
slug: firefox-os-on-nexus-4
comments: true
description: "In this tutorial I will show how to install Firefox OS (also known as Boot to Gecko) on a LG Nexus 4."
authors: ["martinkaptein"]
cat:
  - technology
---


In this tutorial I will show how to install Firefox OS (Boot to Gecko) on a LG Nexus 4.
This post assumes that (just like in my previous post):

- You are rooted
- You have a custom recovery (I had the latest TWRP recovery)
- You have adb, fast boot and device drivers installed on your PC.
- You have a very basic understanding how this stuff works
- You made backups (since you will lose all data)
- If you brick your device I am not responsible

Without further a do, here we go!



## Installing Firefox OS
 
This tutorial is basically the same as [the post on XDA-Developers](https://forum.xda-developers.com/nexus-4/general/june-09-firefoxos-nexus-4-1-1-2-0-t2388237).
If the links don’t work, feel free to [contact](/contact/) me, I will upload this stuff to Dropbox or something.
Download the Firefox OS zip file [here](https://forum.xda-developers.com/devdb/project/dl/?id=9351).


After that, transfer the file to your device, using any method you are comfortable with (for example `adb push`).

Now, boot your device to recovery, wipe the cache, and install the Firefox OS zip you just downloaded. Then restart your device, and wait patiently: It should boot now.

![installing the zips](/images/installing_zip_firefox.jpg)

*installing the zip file*

Firefox OS should boot just fine.

It should be noted, that everything is extremely buggy.

For more information you should see the [the post on XDA-Developers](https://forum.xda-developers.com/nexus-4/general/june-09-firefoxos-nexus-4-1-1-2-0-t2388237).

## Firefox OS on Nexus 4 in action.

![Firefox OS on Nexus 4 in action 1](/images/firefox-os-in-action-1.jpg)
![Firefox OS on Nexus 4 in action 2](/images/firefox-os-in-action-2.jpg)

*Firefox OS on Nexus 4 in action*


## Conclusion

This is a very nice way, to get a glimpse at Firefox OS. Also, mind that the system has a lot of bugs and isn’t supported anymore.
