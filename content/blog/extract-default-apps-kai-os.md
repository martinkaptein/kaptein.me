---
title: "Extracting apps from KaiOS using ADB"
date: 2019-07-30
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - KaiOS
  - Mobile Developement
  - ADB
  - Nokia 8110
slug: extract-default-apps-kai-os
comments: true
description: "How to extract apps from a KaiOS device using the ADB protocol. As an example how to transfer the Snake game and run it locally on your computer."
authors: ["martinkaptein"]
cat:
  - technology
---

## Update 13 Dec 2021

I receive a lot of mails nowadays, regarding things that work differently now (/stopped working), than they did when I wrote this post.
Unfortunately I don't have time now to dive deeper in this topic anymore, so please don't send me questions, most likely you will not receive a reply from me.
This blog post will still be left online for archival and who knows it still might be useful for some.
With this out of the way, here comes the original post:

This blog post is a continuation of my exploration of my KaiOS device, a Nokia 8110 4G and the KaiOS platform. While, it might be not really necessary to be able to do I thought it would be interesting, to see, how to transfer the default KaiOS WebApps via the ADB protocol to your computer, and run them there.

The cool thing with that is, that you can thoroughly examine all the apps (for example the default apps) see their source code and modify it. Of course, since it is a WebApp, it will run just fine on your computer, regardless of the operating system you are using. 

Even, you might get these apps running on an android or iOS device, with a browser wrapper or something. Again, is it really necessary? Probably not, but it is still a cool thing to explore, especially for people getting into mobile app development.

As I have stated in my other posts, I am a big enthusiast of the KaiOS platform.

But anyway, let's get started!


## The setup

Luckily, for this procedure we will not need a WebIDE (however, I you want to transfer an app back to your phone you will, for that you can consult this post.

The only thing we need, is ADB. Please make sure it is installed correctly, there are plenty of tutorials out there for any platform.

Anyway, put your KaiOS phone into debug mode, using this code: `*#*#33284#*#*` (think of it as `*#*#debug#*#*`), and connect it to your computer.

Run `adb devices`, in the Terminal of your choice, to make sure it is connected. If you receive an error, go into the KaiOS device settings, then to Storage and enable USB Storage.

Start the adb shell by typing `adb shell`. Change directories into the `/system/b2g/webapps/` folder by typing `cd /system/b2g/webapps/`.

By the way, ADB is capable of much more cool stuff, some time ago I have written a post about ADB which you can find here.

If you type `ls` you can see a list of all the WebApps installed on your KaiOS device.


## Transferring Snake from the KaiOS device to the computer via ADB

Let's say, we wanted to transfer the Snake game back to our computer. In this the package name would be `snake.gaiamobile.org`.

To transfer it to your computer, open a new Terminal window (local) and create a directory where you want it to be (don't run this from inside the adb shell).

`mkdir snake`

Now, let's pull it in using ADB:

```
adb pull /system/b2g/webapps/snake.gaiamobile.org
```

Of course, if you would want to transfer a different app, you would substitute that name for Snake instead.

Now, on your computer, inside your working directory, you should have a folder called `snake.gaiamobile.org`. Inside this folder are 2 files, `application.zip` and `manifest.webapp`. In this case we just care about the .zip file.

If you unzip the `application.zip` you will see the source code on your computer.

## Running the KaiOS WebApp locally using a WebServer

To run this app locally on your computer you can `cd` into the application folder and start a simple WebServer.

Either `php -S 127.0.0.1:8000`

Or `python -m SimpleHTTPServer`

or `python -m http.server`.

Alternatively, you can use this fork of the python server (ftransfer), which is a lot easier to use (which I made myself).

Now, open your browser, and head over to `http://127.0.0.1:8000` (or a different address and port, whatever).

You should now be able to play Snake in your browser of choice on your computer.

![KaiOS Snake WebApp running locally](/images/blog/kai-os-snake-local.jpg)

*KaiOS Snake WebApp running locally*

You also can explore, how the app is coded, and make modifications to it, how cool is that?
And of course, explore other apps as well.


## WebApps are amazing

This is the amazing thing about WebApps, they just work everywhere (well, depends on the exact technologies and browser specs) - in theory at least.
