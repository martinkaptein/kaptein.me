---
title: "Remove default pre-installed bloatware apps and from KaiOS on a Nokia 8110 4G "
date: 2019-10-01T15:57:17+02:00
lastmod: 2019-10-01T15:57:17+02:00
draft: false
categories:
  - Software
tags:
  - KaiOS
  - bloatware
  - remove
  - Nokia 8110
slug: kai-os-remove-default-pre-installed-bloatware-apps
comments: true
description: "Removing default pre-installed apps and bloatware games on KaiOS is quite simple, especially using temporary root. This requires editing the webapps json file. In this guide the Nokia 8110 4G is used."
authors: ["martinkaptein"]
cat:
  - technology
---

## Update 13 Dec 2021

I receive a lot of mails nowadays, regarding things that work differently now (/stopped working), than they did when I wrote this post.
Unfortunately I don't have time now to dive deeper in this topic anymore, so please don't send me questions, most likely you will not receive a reply from me.
This blog post will still be left online for archival and who knows it still might be useful for some.
With this out of the way, here comes the original post:

In this post I would like to take a look at how to remove annoying pre-installed / default apps from a KaiOS device. In this case the Nokia 8110 4G will be used, but this guide should work on all KaiOs devices.

This will require us to use at least a temporary root option, but don't worry, the process is much more simple than it sounds:)
Finally we will be able to get rid of the annoying pre-installed demo games such as Danger Dash, Castle of Magic and more!

## KaiOS temporary root

The first step is to get (temporary) root permissions on our KaiOS device. For this we will use **Wallace Lite** (since our Nokia 8110 4G comes with busybox installed). If you have a different device, you may have to use **Wallace**. You can download both **Wallace** and **Wallace lite** from [this page at bananahackers](https://sites.google.com/view/bananahackers/root/temporary-root).

The downloaded file will be a .zip file, which is basically a packaged web-app. We will need to install this app on our KaiOS device.

### Nokia 8110 temporary root

Unzip the wallace or wallace lite .zip file and install it to your KaiOS device [using this detailed guide I have written earlier](../sideloading-and-deploying-apps-to-kai-os/).

![Wallace lite running on the Nokia 8110 4G](/images/blog/wallace-lite-kaios-n8110.jpg)

*Wallace lite running on the Nokia 8110 4G*


Then, just run the app. After you launched it you will need to press the center DPAD key and wait until use see this face (from Bladerunner).

![KaiOS temporary root achieved](/images/blog/wallace-lite-n8110-temp-root.jpg)

*KaiOS temporary root achieved*

Now we have temporary root, which will last until the next reboot. Easy, right?

You can verify that you have by starting the adb shell `adb shell`. You should see this:

`root@Nokia 8110 4G:/ #`

(make sure to exit the shell using `exit`)

## Removing bloatware

Now we are getting to the fun part of removing the KaiOS bloatware in the form of pre-installed apps or games.
First of all, we need to transfer the webapps.json file to our computer.

This file is located in /data which was previously not accessible for us. Just pull it using:
```
adb pull data/local/webapps/webapps.json
```

There, is also an other webapps.json file located in /system, but it's not the one we need (because in /system/b2g/webapps is the cache).

Make a backup of this webapps.json file and save it somewhere else. In the case you make a mistake you can always revert to it.

Just open the webapps.json file using your favourite text editor.

### Editing webapp.json

You will see a long list (in json format) of all installed apps. Scroll down until you will see the package name of the app that you want to remove.

Usually the package name looks like the name of the app for example Snake is `snake.gaiamobile.org` etc. However, sometimes the package name is a long string of letters and numbers, in that case you will have to look at the manifest url or other json parameters.

Anyway, when you have found your package just set `"removable": false,` to `"removable": true,`.

If you don't see the *removable* parameter, you can just add it manually, after the `"id":` parameter. Just pay attention to the JSON formatting, that it is correct (for example don't forget the *comma* (only when it is the last parameter you should leave it out)).

Also, make sure to not remove anything vitally important!

Make sure to save your changes, and double check, because in the next step we are going to overwrite the original webapps.json file.

## Transferring the webapps.json file back to our KaiOS device

Transferring the modified webapps.json file is easy.

**This will overwrite the original webapps.json file**

 Just use: 

```
adb push webapps.json data/local/webapps/webapps.json
```

After that you will need to reboot your device. From your computer you can enter the adb shell and run the reboot command:

```
> adb shell
root@Nokia 8110 4G:/ # reboot
```

Now you can just uninstall your app through the menu as usual!

![Uninstall menu on KaiOS](/images/blog/kai-os-uninstall-menu.jpg)

*Uninstall menu on KaiOS*
