---
title: "Converting and Porting Web apps to KaiOS"
date: 2019-07-28
lastmod: 2019-09-21
draft: false
categories:
  - Programming
tags:
  - KaiOS
  - Mobile
  - developement
  - website
  - web apps
  - Nokia 8110
slug: porting-converting-web-apps-website-to-kai-os
comments: true
description: "Converting web apps or websites to KaiOS on a Nokia 8110 4G without Jailbreak or a custom ROM. Porting a web app or website to a KaiOS app."
authors: ["martinkaptein"]
cat:
  - technology
---

## Update 13 Dec 2021

I receive a lot of mails nowadays, regarding things that work differently now (/stopped working), than they did when I wrote this post.
Unfortunately I don't have time now to dive deeper in this topic anymore, so please don't send me questions, most likely you will not receive a reply from me.
This blog post will still be left online for archival and who knows it still might be useful for some.
With this out of the way, here comes the original post:

In this blog post I would like to take a look at how to easily convert port an existing WebApp to KaiOS without Jailbreak or a custom ROM (like [GerdaOS](https://gerda.tech/)). Basically it is about how to port a webapp, website or even FirefoxOS app to a KaiOS app.

If you would like to read how to deploy or sideload this app to your KaiOS, please read [this post](../sideloading-and-deploying-apps-to-kai-os/).


## KaiOS apps

Before we start, we have to answer the question what are KaiOS apps. Fortunately, the answer is very simple as **KaiOS are very simple webapps**.

This is the thing which is so fascinating about the KaiOS platform. It is so incredibly easy to develop apps for it.


### Apps can be websites

Basically, apps can literary be websites. Amazing, right? 

## manifest.webapp

You will only add 1 key file, which will make this website or WebApp work on KaiOS. This file is the `manifest.webapp` file.

If you want to convert a website to a KaiOS you will just need to add this one file to make it work on your KaiOS device (in my case it is going to be the Nokia 8110 4G).

## Converting a website to a KaiOS app

So, you have a finished website. Usually, the website "starts" from the `index.html` file. Then, there are (probably) `css/` `js/` etc. folders with code and content.

We keep everything as is, just make sure to pay attention to a couple of things:

- Your website should scale well (other wise it will be a challenge to use it on such a small screen)
- All content should be relative (that should be the case, if your website is well coded).

Anyway, make a new folder and place all the website files there, with all the content and respective sub-folder structure.

Of course, the index.html file should be in the root directory.


### Adding the manifest.webapp

Now add a `manifest.webapp` to the root directory. 

This file should contain (at least) the following parameters:

```
{
  "name": "app name here",
  "description": "A description.",
  "launch_path": "/index.html",
  "icons": {
    "512": "/img/icon-512.png",
    "128": "/icon-128.png"
  },
  "developer": {
    "name": "Your Name",
    "url": "https://yourwebsite/"
  },
  "default_locale": "en",
  "chrome": { "navigation": false },
  "cursor": true,
  "ime_default_softkey_bar": true
}
```

Save it, and deploy your app using the [post, which you can find here](../sideloading-and-deploying-apps-to-kai-os/). Obviously, it would be nice to add some icons for the launcher.


## Solving issues

There are several challenges, and issues which were surprisingly badly documented.


### Adding dpad navigation

One of the biggest challenges of getting a WebApp to work on my KaiOS device was the navigation in the WebApp (or website) using the directional pad (d-pad).

There are JS frameworks which should help with that, but that was far too much work.

Much easier, although not necessarily user friendly, is just to enable the cursor. We can do this with the 
`"cursor": true` parameter in the manifest.webapp file (which you can see in the example above).

Now, you can navigate your app using the D-Pad on your device.


### Leaving text fields

Another important issue to solve was the fact, that once in text edit mode, it was impossible to leave.

Turns out, that is also very easy to fix with the `"ime_default_softkey_bar": true` parameter in the manifest.webapp file.


## Running any WebApp on KaiOS

There are millions of open source WebApps available. And it is incredibly easy to run any of them on your KaiOS device! Moreover, it is very easy to make adjustments to the source code and deploy it without compiling, or any complicated installations on your system.

These are reasons I absolutely love KaiOS, and I think is has a lot of potential.

Let's consider a practical example:


## Example

I would like to use my KaiOS powered Nokia 8110 4G daily. One app, that I absolutely need, is an Authenticator app (like Google Authenticator), that will generate login TOTP codes, so I can log in to my accounts (time based one time passwords).

At the time of writing, there are no such apps available, not in the KaiOS store (which contains a laughable collection of apps by the way) nor as a packaged KaiOS app.

So, let's find a webapp and convert it for our device!


### Google Authenticator for KaiOS on Nokia 8110 4G

A fantastic WebApp (it is basically a website) for Two-factor authentication can be found [here](https://github.com/gbraad/gauth/).

Let's convert it now!

First of all download the source code, either as a .zip file or `git clone` it.

Make sure to unzip it:)

Luckily for us, it already contains a manifest.webapp file, as well as a set of icons. So we don't even need to worry about that. If it wouldn't have contained a manifest.webapp file, we could just create it ourselves.

Just add the above described parameters to the manifest.webapp. 
Again, the important stuff, that will make it work are the 

```
  "cursor": true,
  "ime_default_softkey_bar": true
```

parameters.

The finished file should look similar to this:

```
{
  "name": "GAuth",
  "description": "A simple application which generates TOTP tokens when multi-factor authentication is used with your Google account. It implements RFC4226 (HMAC-based OTP) and has been tested to work with Google Authenticator, Dropbox, Dreamhost and Amazon.",
  "version": "0.9.9",
  "launch_path": "/index.html",
  "appcache_path": "/cache.manifest",
  "icons": {
    "16": "/img/icon_16.png",
    "48": "/img/icon_48.png",
    "128": "/img/icon_128.png",
    "256": "/img/icon_256.png",
    "512": "/img/icon_512.png"
  },
  "installs_allowed_from": [
    "*"
  ],
  "developer": {
    "name": "Gerard Braad",
    "url": "http://gbraad.nl"
  },
  "cursor": true,
  "ime_default_softkey_bar": true
}
```

![manifest.webapp screenshot](/images/blog/manifest-webapp-screenshot.jpg)

*manifest.webapp screenshot*

Save the file!

Now, you can just deploy the app to your device, [using the method described here](../sideloading-and-deploying-apps-to-kai-os/).


### Screenshots Authenticator for KaiOS on Nokia 8110 4G

![KaiOS Nokia 8110 launcher custom icon](/images/blog/kai-os-launcher-custom-gauth.jpg)

*KaiOS Nokia 8110 launcher custom icon*

![KaiOS TOTP authenticator running on Nokia 8110 4G](/images/blog/kai-os-totp-app.jpg)

*KaiOS TOTP authenticator running on Nokia 8110 4G*


### Modifying the WebApp

While we are at it, let's make a few adjustments in our example, just to see how incredibly easy it is.

Since, this app is an TOTP app, we should actually have to enter the secret by hand. But on a T9 keyboard this really could take ages.

Let's make our task a bit easier.

In the gauth app navigate to the `js/gauth.js` file.

In it, you will see the following code, if you scroll down.

`addAccount('accountname', 'secret');`

![WebIDE source code GAuth](/images/blog/WebIDE-source-code.jpg)

*WebIDE source code GAuth*

You can very simply modify it, and add additional functions below. There you can enter your data:

```
addAccount('gmail', '9r8uv40rybv');
addAccount('outlook', 'ifuy47br3847ryb398');
addAccount('facebook', 'r982nckj');
```

Just make sure to remove whitespaces in the secret code if there are any.

Now, re-deploy the GAuth app to your KaiOS device. Voila! 


## Conclusion

The beauty of KaiOS is the fact, that it is so easy to play with it, to install your own apps, without any complicated IDE. Not only in developing markets, but also in developed markets it is a great smartphone operating system to get someone into programming, in a very accessible way.

I have really high hopes for KaiOS, and hope, that it will become a major player in the smartphone environment, without sacrificing the openness and legacy it has inherited from FirefoxOS.
