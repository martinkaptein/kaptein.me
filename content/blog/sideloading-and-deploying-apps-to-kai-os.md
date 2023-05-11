---
title: "Side-loading and deploying custom apps to KaiOS"
date: 2019-07-28
lastmod: 2019-10-1
draft: false
categories:
  - Software
tags:
  - KaiOS
  - mobile
  - Nokia 8110
  - sideloading
  - web apps
  - tutorial
slug: sideloading-and-deploying-apps-to-kai-os
comments: true
description: "Side-loading and deploying custom apps or zip files to KaiOS without a Jailbreak or OmniSD. For this we will use WebIDE which allows us to seamlessly install a webapp on our KaiOS device."
authors: ["martinkaptein"]
cat:
  - technology
---


## Update 13 Dec 2021

I receive a lot of mails nowadays, regarding things that work differently now (/stopped working), than they did when I wrote this post.
Unfortunately I don't have time now to dive deeper in this topic anymore, so please don't send me questions, most likely you will not receive a reply from me.
This blog post will still be left online for archival and who knows it still might be useful for some.
With this out of the way, here comes the original post:

In this blog post we will be side-loading and deploying a custom WebApp (which can be a FirefoxOS app, by the way) to our KaiOS device without a Jailbreak or OmniSD.

The process is very similar to the process, which is outlined on [BananaHackers here](https://sites.google.com/view/bananahackers/install-omnisd/sideload-using-webide).

Make sure to check out [this post](../porting-converting-web-apps-website-to-kai-os/) with information on [how you can easily convert a website or WebApp to a KaiOS app](../porting-converting-web-apps-website-to-kai-os/). How to deploy such an app, will be described in the following.


## What we need


### Device

First of all we will need (obviously) a KaiOS device. In this case I will be using the **Nokia 8110 4G**.


### Software

What I absolutely love about the KaiOS platform, is how easy it is to develop and deploy applications for it. We will only need:

- adb (installation instruction [here](https://lifehacker.com/the-easiest-way-to-install-androids-adb-and-fastboot-to-1586992378))
- Firefox 52.9 or older (recommended Firefox 49) OR
- [Pale Moon browser](https://www.palemoon.org/)

Personally, since it is quite annoying to install an outdated version of Firefox, I decided to use Pale Moon browser on Linux (via a VM on MacOS). That worked flawlessly.

**UPDATE**

Pale Moon browser decided to remove the precious WebIDE functionality (which we very much need) from their browser, in their latest versions.
Now, you will have to use an [older version of Palemoon](http://archive.palemoon.org/palemoon/28.x/28.6.1/), which you can find [here](http://archive.palemoon.org/palemoon/28.x/28.6.1/).
The rest of the procedure stays the same.

#### Why Firefox

Just in case you are wondering, KaiOS is based on Firefox OS (Boot to Gecko) which is, very sadly, discontinued. The most amazing (in my opinion) thing about this platform is the fact, that it is so easy to write apps for it.

The only thing, you will need to be familiar with (if you want to write apps from scratch) is HTML5 and Javascript. The app can *literary* be a website running like an app on your phone.

In the following we are going to do that on our KaiOS device.


## KaiOS developer mode

Basically, my steps are very similar to those found on [BananaHackers](https://sites.google.com/view/bananahackers/home).


### Debug mode

First, we will need to enable debug mode. That's very easy:

Just enter `*#*#33284#*#*` on the keypad from the home screen (to memorise it you can think of `*#*#debug#*#*`). A bug should appear on the top of the screen.


### ADB

Now we can just connect our device using ADB (assumes you have ADB installed). Just connect it using a USB cable and check for the device using `adb devices` (from the terminal or command line).


#### ADB error, no permissions

![adb error screenshot](/images/blog/adb-error.jpg)

*adb error screenshot*

It could happen that you get the following error: `no permissions (user in plugdev group; ...)`. For me this only happened on Linux. To fix this *no permissions, user in plugdev group* error, just head on your KaiOS device into the settings, then go to *Storage* and enable *USB Storage*.

Then restart the adb server using `adb kill-server` (from Terminal) and run `adb devices`again (like shown on the screenshot).


## Connecting to Pale Moon Browser

Alright, now we can connect our device to the Pale Moon Browser (or an outdated Firefox version, if you chose for that - the process is exactly the same).


### WebIDE

Fire up your Pale Moon and head over to *Tools* >> *Web Developer* >> *WebIDE*.

Then click on *Remote Runtime*. Check, that it says `localhost:6000` and press *connect*.


#### WebIDE error

Now it is very likely that it will say *Operation failed: Connecting to Remote Runtime*.

![WebIDE error](/images/blog/web-ide-error.jpg)

*WebIDE error*

In this case just run the following from your Terminal:
```
adb forward tcp:6000 localfilesystem:/data/local/debugger-socket
```


## Opening packaged web app 

If your web app comes in a packaged format (in a .zip file) you will have to unzip it.

In the Pale Moon WebIDE click on *Open packaged App...* and head inside the directory where the app is located, more specifically the `manifest.webapp`file. Click open.


## Deploying app to the KaiOS device

If everything is well you should see green circle next to the app title. If you don't see it, that is not necessarily a big deal, because the WebIDE environment checks for the necessary requirements as if it were an app for FirefoxOS. Of course, KaiOS will have slightly different requirements. 

Just press the play button (the triangle button) and your app should deploy to your KaiOS device.

If you want to learn how to actually convert a usual website or web app to KaiOS format, please check out [this post by me](../porting-converting-web-apps-website-to-kai-os/).
