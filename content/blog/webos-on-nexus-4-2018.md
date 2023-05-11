---
title: "WebOS reincarnated on LG Nexus 4 as LuneOS"
date: 2018-04-02
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - smartphone
  - mobile
  - webOS
  - palm pre
  - nexus 4
slug: webos-on-nexus-4-2018
comments: true
description: "Running a ported version of WebOS (LuneOS) on the LG Nexus 4. Installation instructions, comparison with Palm Pre Plus and my impressions."
authors: ["martinkaptein"]
cat:
  - technology
---


As a big enthusiast of WebOS and as a proud (and somewhat nostalgic) owner of a Palm Pre Plus I was massively surprised, when I heard that WebOS is still alive and has been ported to the LG Nexus 4.

So, without further a do, I will report about my experience with it.

## Installation of LuneOS on LG Nexus 4

The installation is relatively straightforward and instructions can be found [here](http://webos-ports.org/wiki/Mako_Info).

To sum up:

Download [CM12](https://www.androidfilehost.com/?fid=457095661767139495) and [LuneOS](http://build.webos-ports.org/releases/decaf/images/mako/).

Make sure your device is rooted and the boot loader is unlocked.
 
Flash a recovery (I used TWRP) and copy both .zip files you just downloaded to the phone (`adb push`) while in recovery.
Make sure to do a full wipe before that.

Now, first install the cm-12.1xx.zip and directly after that (without rebooting) the LuneOS .zip. After that reboot!

Done!

## My impression

Admittedly I am a very big WebOS enthusiast, and still think it is one of the best operating systems for a mobile device in terms of User Interface. 

It is funny to see how, still, many years later manufacturers draw inspiration from it (cough-cough iPhone X).

In the old days, I used my Palm Pre Plus very extensively, and am still coming back to it regularly.

However, the LuneOS port for the Nexus 4 still seems incredibly buggy. I encountered several instances, when the screen began suddenly flashing. Also, some random shutdowns.

The system works relatively fluently, although, as an example, when scrolling, you can frequently see some element redrawing artefacts. 
Also, the interface looks, still, very alpha. For example, many icons are blurred, there are inconsistencies in text size and, generally speaking, in the design of the apps and the whole system.

For example the camera app:

![LuneOS camera app Nexus 4 vs Palm Pre Plus](/images/blog/luneos-camera-1.jpg)

![LuneOS camera app Nexus 4 vs Palm Pre Plus 2](/images/blog/luneos-camera-2.jpg)

*Camera apps compared between LuneOS on Nexus for and WebOS on Palm Pre Plus.*

There are many developer tools pre-installed, it is fun to play around with them.

Also, the developers had quite some sense of humour:

![Settings LuneOS on LG Nexus 4](/images/blog/luneos-dev-humour.jpg)

*Settings LuneOS on LG Nexus 4*

Here are a couple of more pictures:

![Web Browser LuneOS Nexus 4 and Palm Pre Plus](/images/blog/luneos-browser.jpg)

*Web Browser LuneOS Nexus 4 and Palm Pre Plus*

![Terminal on Lune OS on Nexus 4](/images/blog/luneos-terminal.jpg)

*Terminal on Lune OS on Nexus 4*

## Verdict

To make LuneOS a finished consumer-oriented product there is still a lot of work to be done.

Sure, I didn’t report about technical beneath-the-surface stuff, but nevertheless that was my first impression.
However, that said, it has been incredibly nice to see that WebOS is still alive and people are still enthusiastic about it!

Hats off to the developers and active community of LuneOS. Respect!

Who knows, what the future will bring?
