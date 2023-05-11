---
title: "Playing around with ADB"
date: 2018-05-20
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - developement
  - ADB
  - android
  - command line
  - terminal
slug: playing-around-with-adb
comments: true
description: "Playing around with Android Debug Bridge, finding out its amazing possibilities: The remote ADB shell, screen recording, remote app installation and much more."
authors: ["martinkaptein"]
cat:
  - technology
---


In this Blog post, I would like to take a look at ADB, which stands for Android Debug Bridge. It is a tool, which can do a surprising amount of stuff, which I was pleased to discover.

This is an introduction to ADB.

For this, I am going to use my Nexus 4, about which I have already written a lot of posts running the latest Lineage OS (at the time of writing it’s 15.1), which corresponds to Android 8.1 (which is quite amazing for such an old device, isn’t it).

I am not really sure whether other devices also support stuff like ADB over network in their stock rom (please let me know in the comments). 

Anyway, this post is just about my experiences with ADB so far, besides the usual commands the modders and rooters from you already know for sure.

##  ADB installation on MacOS, Windows or Linux

The ADB command line tools are incredibly easy to install: Just download [the zip file for your platform here](https://www.xda-developers.com/install-adb-windows-macos-linux/), extract it and `cd` into it from your terminal or command line.

You can add it to your `$PATH` for convenience.
On MacOS you can alternatively use homebrew to install the android platform tools (ADB):

```
(assuming you already have homebrew installed)

brew tap caskroom/cask
brew cask install android-platform-tools
```

On Debian use:
`sudo apt-get install adb`

Run `adb devices` to check whether ADB has been installed successfully.

Now, let’s get to the meat.

## Useful ADB goodness

### ADB shell access over network

I was very pleased to find that I don’t need to physically connect my android phone to the computer in order to access the ADB shell. 

Activate *ADB over network* in the Developer options of our phone. You will see your local IP address and port.

![screenshot of Developer options in Android](/images/blog/adb-dev-options-screenshot.jpg)

*screenshot of Developer options in Android* 

**Warning: Deactivate this options as soon as you don’t need it anymore or if you don’t trust your network - anyone could gain access to your phone now!**

On your computer type:

```
adb connect 192.168.178.68:5555
adb shell
```

Now you will be in the ADB shell of the phone, without connecting it physically.

Type `ls /sdcard/` to see the contents of your home directory on your phone.

**Note:** If you get *permission denied* errors, it means that ADB has no root access on your phone. However, we won’t need it yet anyway.


Here you can use the power of your most favourite UNIX terminal commands.

Taking a look in the `/system/bin` directory reveals more information.

Type `ls /system/bin` to view all of the commands.

Here you will find a lot of interesting stuff.

## ADB screen recording via remote shell

For example you can record the screen of your phone directly from your computer (remote shell):

`mako:/ $ screenrecord /sdcard/outputfile.mp4`

This will start to record a video of the screen of your phone. Press `CTRL+C` to stop the recording process.

The recording will be saved in the home directory (/sdcard/) of your phone, which you can view with any android file manager.
Using other directories might throw `Read-only file system` errors.

Or you can exit the shell and transfer the recording to your computer:

```
mako:/ $ exit
> adb pull /sdcard/outputfile.mp4
```

## ADB remote app installation

Another handy feature of ADB is its ability to install apps. Of course that also works remotely.

Say you downloaded some .apk files on your computer, and want to directly install them on your android device.

Make sure that your phone is still connected using `adb devices`. If not, connect the phone again using `adb connect ipadress:port`.

Navigate to the place where you have your apk’s : `cd your/dir`.

Now you can remotely install your app using `adb install appname.apk`.

## Conclusion

This is just the tip of the iceberg, there a great many more features that ADB offers. It’s very powerful. This openness is one of the biggest benefits of android, there are just so many possibilities. Sure, it opens attack vectors, but as they say:

> With great power comes great responsibility.

And that applies to Android, and, broadly speaking, technology as well.

This was just a brief introduction to the Android Debug Bridge protocol, there is much more, so hack away.

I really hope to have some time in the future, to take a more in-depth look at the “hidden” features of android. These features really can make life easier.
