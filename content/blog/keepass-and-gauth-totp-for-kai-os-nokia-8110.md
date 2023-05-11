---
title: "KeePass and TOTP Authenticator for KaiOS on the Nokia 8110"
date: 2019-07-30
lastmod: 2019-09-21
draft: false
categories:
  - Programming
tags:
  - KaiOS
  - Mobile
  - Porting
  - Nokia 8110
  - KeePass
  - Authenticator
slug: keepass-and-gauth-totp-for-kai-os-nokia-8110
comments: true
description: "Installing a KeePass and TOTP Authenticator client on KaiOS on the Nokia 8110 4G. In this case we will be porting existing webapps for KeePass and Google Authenticator to KaiOS and make them work on the Nokia device."
authors: ["martinkaptein"]
cat:
  - technology
---

## Update 13 Dec 2021

I receive a lot of mails nowadays, regarding things that work differently now (/stopped working), than they did when I wrote this post.
Unfortunately I don't have time now to dive deeper in this topic anymore, so please don't send me questions, most likely you will not receive a reply from me.
This blog post will still be left online for archival and who knows it still might be useful for some.
With this out of the way, here comes the original post:

The KaiOS-powered Nokia 8110 4G is an amazing phone for a very good price. So much so, that I would really like to use it as my main phone.

However, there are two (open source) services on which I very much rely, and which are not available on the KaiOS platform for the Nokia 8110 4G (at least, at the time of writing this article). These services are **a client for KeePass** (password manager) and **Authenticator** an app for TOTP one time code generator for authentication.

I really need these apps, as it can always happen, that I need to log in to my accounts, and I have only my main phone with me.

In this blog post, I will present an alternative, which worked really well for me, and show you, how to install both a KeePass client as well as a TOTP authenticator (for example Google Authenticator) on your KaiOS device.

This will work on any KaiOS device, but I am going to do it on the Nokia 8110 4G. Let's get started!

 
## The Alternative


### J2ME

One technology, I directly thought about, was having a J2ME app run on KaiOS. I am a big enthusiast of older devices, like Nokia Symbian or Blackberry Bold devices, and they all supported J2ME!

You could even run J2ME apps on the most primitive feature phones!

And of course, there were J2ME KeePass and J2ME Google Authenticator clients. For a KeePass client you had **keepassj2me** and for Time based one-time password generation you had **totp-me**.

I still have those programs around, they still work great!

That's actually the thing about *J2ME*, in my opinion is was one of the best things to happen to mobile phones. A cross-platform system, that united feature phones from all brands! Only thing, it was apparently quite difficult to develop a J2ME app, because you had to make it work on an incredible range of devices.

Anyway, I am getting distracted. Of course there are emulators around, that are making J2ME apps work.

So, since the KaiOS platform *does not* have support for Java apps nor J2ME, the first thing I though of was a J2ME emulator for KaiOS on the Nokia 8110 4G.

#### J2ME on KaiOS

Apparently, there **is** a J2ME emulator available, it can be found [here](https://sites.google.com/view/b-hackers-store/home/emulators). It is called *KAVA* and can be installed, in a [method I am describing here](../sideloading-and-deploying-apps-to-kai-os/).

There is a big "however", however. This emulator is still in beta, and for me after the successful installation, is was just hanging when I tried to start a Java -jar file on my KaiOS device.

I tried to mess with everything, but nothing really worked.

But there is a different, much more elegant solution!

## The solution is a web app!

Of course! KaiOS is based on Firefox OS Boot to Gecko. It can run Web apps natively.

While it is really sad, that our Nokia 8110 4G running KaiOS can not run J2ME, Java or jar files, the Web App alternative is actually not a bad thing at all.

If you are not familiar with this technology, you can view this blog post as an introduction to WebApps on the KaiOS platform. Yes, it is sad that J2ME is dead, but WebApps have the capacity to also be truly cross-platform, and perhaps replace J2ME. In fact, **Web Apps are already cross-platform**!

### WebApp introduction

Basically, you can think of a WebApp as just a website. It has all the necessary files (like .html, .css, .js etc.) and all the media (like text, images etc.).

However, this 'website' is scaled nicely, and has all its main content available offline, locally, on your KaiOS device. That's it! There is just a couple of lines, that have to be added to an extra file, called `manifest.webapp`, to make the Soft Buttons as well as the D-Pad work correctly with your WebApp on your KaiOS device.

Talk about easy!

Actually, if you want to read a more in-depth article about this topic, I [suggest this article, where I write about how to convert a WebApp to KaiOS, and how you can do it easily yourself](../porting-converting-web-apps-website-to-kai-os/).

## KeePass WebApp for KaiOS

Ok, let's get the KeePass client installed on your KaiOS device.

By the way, [here is the homepage of the original developer](https://bitbucket.org/namn/browsepass/src/master/).
[Download it as a .zip file from here](https://bitbucket.org/namn/browsepass/get/c9945ab7f837.zip) and unzip it.

Before installing it on your phone, create a file, in the root directory (where the `index.html` is), called `manifest.webapp`.
In this empty new file post the following code:

```
{
  "name": "KeePass",
  "description": "A read-only, web-enabled version of KeePass.",
  "launch_path": "/index.html",
  "icons": {
    "512": "/img/icon-512.png",
    "128": "/icon-128.png"
  },
  "developer": {
    "name": "namn",
    "url": "https://bitbucket.org/namn/browsepassg"
  },
  "default_locale": "en",
  "chrome": { "navigation": false },
  "cursor": true,
  "ime_default_softkey_bar": true
}
```
Save this file, and deploy the WebApp with the method [the method I am describing here](../sideloading-and-deploying-apps-to-kai-os/) (recommended).

What this file does, it just 'tells' the KaiOS system to enable the D-Pad cursor (so you can navigate the app) and enables the soft-keys (for example to exit a text field, which is kind of important).
Alternatively, it would also work with OmniSD, but I haven't tested that. In that case you should zip the app again.

Here are a few screenshots of a KeePass WebApp running on KaiOS:

![KeePass icon in the launcher](/images/blog/keepass-kai-os-launcher.jpg)

*KeePass icon in the launcher*

![KeePass WebApp running on KaiOS on the Nokia 8110 4G](/images/blog/keepass-on-kai-os.jpg)

*KeePass WebApp running on KaiOS on the Nokia 8110 4G*

In my experience this works very well, and is perfectly usable!


## GAuth WebApp for KaiOS

For the TOTP authenticator WebApp the procedure is exactly the same. You can download it as a [.zip file from here](https://github.com/gbraad/gauth/archive/master.zip).

Again, credit goes to [gbrad](https://gauth.apps.gbraad.nl/).


Paste this code into the `manifest.webapp` file:

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

Again, install it either with OmniSD or with [the method I am describing here](../sideloading-and-deploying-apps-to-kai-os/) (recommended). 

Here are a few screenshots of the GAuth WebApp running on KaiOS:

![GAuth in KaiOS launcher](/images/blog/gauth-launcher-kaios.jpg)

*GAuth in KaiOS launcher*

![GAuth TOTP code generator in KaiOS on the Nokia 8110 4G](/images/blog/g-auth-nokia-8110-kai-os.jpg)

*GAuth TOTP code generator in KaiOS on the Nokia 8110 4G*

![GAuth preferences KaiOS](/images/blog/gauth-preferences-kaios.jpg)

*GAuth preferences KaiOS*

This app also works perfectly, as if it has been developed for this system.


## Conclusion

It is very easy, to make WebApps work on KaiOS. Again, to read more about the latter [check out this in-depth post](../porting-converting-web-apps-website-to-kai-os/).
I really think very positively about the future of KaiOS and the concept of WebApps (thanks to Firefox, actually).
