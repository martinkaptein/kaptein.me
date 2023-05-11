---
title: "How to unlock the Google Pixel bootloader and flash a custom rom with root"
date: 2019-07-11
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - Smartphone
  - Google Pixel
  - LineageOS
  - custom rom
slug: flashing-lineageos-on-the-google-pixel-with-root-in-2019
comments: true
description: "How to flash Lineage OS on the Google Pixel with root in 2019 using temporary boot of TWRP."
authors: ["martinkaptein"]
cat:
  - technology
---


<p> This post and the next posts will be dedicated to the original Google Pixel phone.</p>
<p>Precisely, in this post I will be explaining how to unlock the Google Pixel and how to flash a custom rom, we will be using <a href="https://lineageos.org/" target="_blank" rel="noopener noreferrer">LineageOS</a>.</p>
<p>This process is not as simple as it used to be, because of many reasons, including slots and the <a href="https://www.reddit.com/r/LineageOS/comments/b3g3fi/ab_twrp_how_do_the_slots_actually_work/" title="partition explanation on reddit" target="_blank" rel="noopener noreferrer">A/B partition situation</a> with TWRP recovery. For some reason it was difficult to find a clear explanation on how to do it in the year 2019. I remember reading <a href="https://lineageos.org/Changelog-19/" title="LineageOS blog post" target="_blank" rel="noopener noreferrer">this LineageOS blog post</a>, which helped me a lot. Moreover, <a href="https://www.reddit.com/r/LineageOS/comments/b3g3fi/ab_twrp_how_do_the_slots_actually_work/" title="explanatory reddit post" target="_blank" rel="noopener noreferrer">this reddit post, explains it quite well</a>, but is complicated. Maybe Google has changed some stuff since this phone first launched, since so many tutorials seem outdated and didn't work for me.</p>
<p>For me it took a lot of tries to figure it out. At one time I even had to return to stock. </p>
<p><strong>By the way, I am not responsible for a bricked phone! Please be careful!</strong></p>
<p>I assume that you have adb and fastboot, plus the drivers correctly installed on your computer. If you need more help with that take a look at</p>
<a href="https://www.xda-developers.com/install-adb-windows-macos-linux/" title="ADB installation tutorial" target="_blank" rel="noopener noreferrer">this tutorial on XDA developers.  </a>
<p>If you already tried to flash something, it would make sense to return your Google Pixel back to stock completely (and discover the reason why a custom rom is so much better haha). Personally, I started from the February 2019 stock situation.</p>
<p>By the way, returning your Google Pixel to stock, re-locking and un-rooting it, is not that diffecult. <a href="https://developers.google.com/android/images" title="How to return Google Pixel back to stock" target="_blank" rel="noopener noreferrer">This Google site does a very good job explaining how to return your Google Pixel to stock</a>, whilst removing root, and locking it.</p>
<p>Anyway, starting from the stock, un-unlocked and un-rooted situation:</p>
<p>First of all, setup the phone like normally, <strong>with a passcode</strong> (if you use the fingerprint scanner, you will be prompted for a passcode fallback). Actually, what happens, is that the storage is encrypted with your passcode.</p>
<p>Then enable developer options, by tapping on the build number (in settings) lots of times, and enable (inside the developer options) OEM unlocking. Also enable USB debugging.</p>
Now reboot to the bootloader by running <code>adb reboot bootloader </code>from the command line of your computer.
<p>With your device connected run <code>fastboot flashing unlock</code> on the command line of your computer and confirm the messages. Now reboot the phone. You will need to setup the phone again. Also, use a passcode, same as before.</p>
<p>We are not done yet!</p>
<h4 id="mcetoc_1dattcb1d5">How to flash LineageOS on the Google Pixel</h4>
<p>On your computer <a href="https://eu.dl.twrp.me/sailfish/">download the TWRP recovery</a>. With my method, you will only need the <code>.img</code> file. Actually, this method is documented in <a href="https://lineageos.org/Changelog-19/" title="LineageOS blog post" target="_blank" rel="noopener noreferrer">this lineageos blog</a>. At the time of writing it is the file <code><a href="https://eu.dl.twrp.me/sailfish/twrp-3.3.0-0-sailfish.img.html">twrp-3.3.0-0-sailfish.img</a> </code>. The nice thing is, that TWRP now supports decryption of the device storage.</p>
<p>But hang in there, because now we will have to deal with "slots".</p>
<p>Also, in your working directory, on your computer, download the other files you will need, mainly the lineageos .zip file for the Google Pixel (which has the nickname "sailfish" by the way). Optionally, if you want root access, you will also need the addonsu zip from <a href="https://download.lineageos.org/extras">here</a>. Also, optionally, you can download the Google Apps .zip.</p>
<p>Both OpenGApps and MindTheGApps should work with this method, at the time of writing.</p>
Reboot to the bootloader again, with your Google Pixel connected run <code>fastboot boot twrp... .zip.</code>TWRP will ask for your password, just enter your passcode (this will happen each time).
<p>First of all, make a full wipe (go to advanced, wipe and wipe all). Then reboot to bootloader and boot TWRP (temporarily) again (with the same command as before). You will need to repeat the rebooting of the recovery many times, it has to do with slots. Basically, this is what the lineageos blog was saying. So hang in there!</p>
<p>When you are in TWRP again (2nd time) push the lineageos.zip using <code>adb push lineageoszip.zip /sdcard/ </code>. The<code> /sdcard/</code> doesn't depict any physical sd-card, its just an android convention. Now install the zip normally, like you are used to. DO NOT REBOOT THE SYSTEM!</p>
<p>Reboot TWRP again (reboot to bootloader, and <code>fastboot boot twrp.img</code>, you get the idea). Now (during the 3rd time) push the GApps .zip (optionally) and install the .zip. You will notice, that all files appear to be missing, also the lineageos.zip, which you have pushed previously. Again, boot to bootloader, and boot TWRP, for the last time in order to install the addonsu.zip (4th time).</p>
<p>Now you may reboot the system. You will notice, that every time you boot the system you will see a very ugly warning by Google.</p>
<p><img src="/images/blog/image20190711_153230946.jpg" alt="Google Pixel boot warning message" width="628" height="449"></p>
*Google Pixel boot warning message*
<p>Also, the TWRP recovery is not installable permanently anymore. So every time you want to flash something, you will need to temporarily boot it again.</p>
