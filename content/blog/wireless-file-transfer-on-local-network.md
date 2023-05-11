---
title: "Wireless cross platform file transfer"
date: 2019-02-15
lastmod: 2019-09-21
draft: false
categories:
  - Software
tags:
  - python
  - developement
  - file transfer
  - cross platform
  - server
slug: wireless-file-transfer-on-local-network
comments: true
description: "How to transfer files easily between any device on the local network such as your old phone and your computer using a simple python server with added upload capability."
authors: ["martinkaptein"]
cat:
  - technology
---


# How to transfer files wirelessly to any device in a local network

Recently, I was presented with an interesting challenge: I wanted to transfer files wirelessly in my local network to any device, meaning that any platform should support it.
Basically, I wanted to transfer files between my computer and any device with WLAN and a web browser. So I began searching for a solution, which I will write about in this blog post.

## Cross platform file sharing

So basically, my solution should take care of a few things:

- really easy to use in order to deploy quickly
- no proprietary software (I don't want to depend on anything)
- I want to understand how it works (=open source)
- it should work without an internet connection (only local wifi network)
- it should work on any device with WLAN and a very basic browser


For example I would like to be able to share files between my computer and old WebOS, Windows Phone, Blackberry and Symbian phones (of course iOS and Android as well) . Those phones have very outdated browsers, so my solution should take that into account and not be too fancy. Hence, the solution will be inherently insecure, as those old mobile operating systems don't have the latest certificates and stuff, so please keep that in mind!

## Running a local server with upload capability

The most logical solution is to use some kind of local server, which should be really easy to start. There are many solutions, such as `php -S`, but since I am not *that* familiar with PHP I will use Python. We would just need to run the server on `0.0.0.0` to make it accessible from any device in the local network (as opposed to `127.0.0.1`).

## Python server

Since Python has already a fantastic simple server, which can be invoked with `python -m http.server`, if you have Python 3 (if you have Python 2 you can use python -m SimpleHTTPServer). We would just need to add an upload capability to it.

## Python comes preinstalled on most operating systems 

The advantage of Python is that it comes preinstalled on most UNIX systems, like Linux, OSX or MacOS (and can be installed really easily on Windows). Also, it is just very pleasant to work with as it is very easy to understand.

## Python http.server with upload

With Python comes also the `http.server` (or `SimpleHTTPServer` respectively) bit preinstalled. However, by default it cannot parse POST request. And that we really need to do.

There are a lot of discussions about this topic, for example on [Stack overflow](https://stackoverflow.com/questions/20428514/can-one-upload-files-using-python-simplehttpserver-or-cgi).
Long story short, I have found finished code as a gist on github (you can find it [here](https://gist.github.com/UniIsland/3346170)). This code I have forked into a program called [ftransfer](https://github.com/martinkaptein/python-file-transfer). You can find it and the source code [here](https://github.com/martinkaptein/python-file-transfer). 

## Using ftransfer for easy file transfer in the local network

There are detailed instructions in the [README.md in my repository](https://github.com/martinkaptein/python-file-transfer/blob/master/README.md) about the installation.

It is really as easy as it gets!

Basically, that's it! Just my quick report about how to share files from any device in your local network to your computer. Perhaps I have helped you!

