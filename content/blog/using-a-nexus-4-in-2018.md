---
title: "Using a Nexus 4 in 2018"
date: 2018-03-03
lastmod: 2019-09-21
draft: false
categories:
  - Hardware
tags:
  - android
  - smartphone
  - mobile
  - nexus 4
  - 2018
slug: using-a-nexus-4-in-2018
comments: true
description: "The perks of buying a Nexus 4 phone in 2018. Best custom ROMs for best battery life, running different operating systems (such as Ubuntu Touch, Firefox OS and Sailfish OS) and much more."
authors: ["martinkaptein"]
cat:
  - technology
---


About a month ago, I had the crazy idea of buying a used LG Nexus 4 phone. 

After a while the idea didn’t even seem crazy anymore: The phone is incredible well supported by the community (such as [XDA Developers](https://forum.xda-developers.com/nexus-4) ).

I could run the latest Android version, play around with various Operating Systems that were ported to the Nexus 4, for example Ubuntu Touch, Firefox OS (also known as Boot to Gecko) or even Sailfish OS. 

So I bought it (for a good price, I should notice), off amazon.

In this blog post I will write about my experience with this phone, and the reasons I am incredibly happy with it. 
And also why I think that it is still in 2018 a very usable phone.

## Best custom ROMs for the Nexus 4

### Lineage OS

In the time I had this phone, I have probably installed every single android custom ROM, which I could find on XDA Devs. 

For me, **Lineage OS** was the best option. Whilst it (at the time of writing) doesn’t run the latest Android version, it is very stable and well supported.

Also, out of all the ROMs, I have achieved the best battery live with Lineage OS. In standby, even with GApps installed, it virtually doesn’t drain any battery.

[Here’s a link to the official Lineage OS website](https://www.lineageos.org/)

### Situation with GApps

Very recently, there has been a lot of fuzz because of Google blocking Google Apps on *“uncertified devices”*, [read here](https://www.xda-developers.com/google-blocks-gapps-uncertified-devices-custom-rom-whitelist/). 
For me, there weren’t any problems running it on Lineage OS, according to the play store the device is certified. 


![Playstore device verification Lineage OS](/images/blog/screenshot-nexus4-playstore.jpg)

*Playstore GApps verification on Lineage OS*

## Other Operating Systems on Nexus 4

Until now, I have successfully manage to run [Firefox OS](../firefox-os-on-nexus-4), [Sailfish OS](../sailfish-os-on-nexus-4/) and [Ubuntu Touch](../ubuntu-touch-on-nexus-4-in-2018-installation-and-review/) (UBPorts).

### Firefox OS on Nexus 4

Pretty straightforward installation, see [this post for more information](../firefox-os-on-nexus-4/).
It runs very unstable, and there is barely any practical use to it, especially since the project is long discontinued. But still, nice to play around with it.

### Sailfish on Nexus 4

I liked Sailfish OS a lot, although the way of using the system takes some time getting used to it. For me, the Appstore didn’t work, also bluetooth didn’t. 
[Here you can find instructions on how to install Sailfish OS on the Nexus 4](../sailfish-os-on-nexus-4/).

I was very pleasantly surprised by the easy way to connect to the phone via SSH. Literally on press of a button, with randomly generated passwords. More OS’s should do it that way.

Also, very beautiful system.

### Ubuntu touch on Nexus 4

Last but not least, I would like to write about my experience running Ubuntu Touch on a Nexus 4. **This is a completely different story.**

Installing Ubuntu Touch (obviously UBports version) was a very big pain. 

I ended up doing that through a virtual machine (Virtual Box running ubuntu) on a MacBook. Used the official instructions, which can be found on the UBPorts installer Github page [here](https://github.com/ubports/ubports-installer/tree/0.1.11-beta#how-to-install). Add the udev rules.

Also, if you do it that way, please make sure to use Virtual Box with the USB filters, and don’t forget about the VirtualBox extension pack, without which the usb connection fails shamelessly.

ADB sometimes also acted pretty crazy during the installation progress, had to use `adb kill-server`, then `adb start-server`. Restarting is often the best solution:) 

If this is interesting to you, I will write an in-depth tutorial. Please let me know!

### Ubuntu Touch, Ubports, user experience

I was incredibly surprised by the usability of Ubuntu Touch, everything worked, and I had amazing battery life. 
The system is very well supported, new Apps (Webapps) appear all the time, and according to the ubports website, the Nexus 4 will receive the update to the next LTS release.
This is amazing!!

If you can mind (mostly) the absence of your favourite apps, I can only recommend ubuntu touch. It is a great operating system, with a bright future (I really hope so).

Probably my favourite system I have used so far on any phone (and I have used many, I can tell you that).
Anyway, here is a lot of potential to write very in-depth blog posts about all of these subjects. And I am looking forward to doing that.

Make sure to give Ubuntu Touch a try! These guys are doing amazing work!

![Ubuntu Touch ubports running on Nexus 4](/images/blog/ubuntu-touch-nexus-4.jpg)

*Just an action shot of the Terminal app (rsyncing stuff) in Ubuntu Touch ubports on the LG Nexus 4*

## To sum up

One thing is clear: If you can snatch a LG Nexus 4 (perhaps used) for a good price and if you are a technology enthusiast like me, there is no reason not to! You will be very satisfied.
