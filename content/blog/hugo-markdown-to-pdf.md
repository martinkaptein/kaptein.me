---
title: "Markdown to pdf using Hugo and beautiful styling"
date: 2020-01-05T12:26:23+01:00
lastmod: 2020-01-05T12:26:23+01:00
draft: false
categories:
  - Software
tags:
  - Hugo
  - setup
  - writing
  - markdown
  - pdf
slug: hugo-md-to-pdf
comments: true
description: "How to convert markdown to pdf using Hugo. We will be maintaining beautiful document styling and formatting. This setup is fully portable."
authors: ["martinkaptein"]
cat:
  - technology
---

# Converting markdown to pdf with Hugo

In this post we will be taking a look at how to generate beautifully formatted documents with Hugo.
The idea is to have a markdown to pdf conversion pipeline.

So, let's get started!
 
## Why Hugo

My [previous post](../markdown-to-pdf-without-latex/) was dedicated to a markdown to pdf conversion technique, which involved [pandoc](https://pandoc.org/).
There I explored how to convert markdown to pdf, **without using latex**.

This is purely, to have a very lightweight document writing setup, it is in no way supposed to replace latex.

Hence, in this post we will be doing the same thing, but with [Hugo](https://gohugo.io/).
So why did I choose Hugo?

First of all, Hugo is a fantastic tool for generating static website (and it can do much more than that, rest assured (there will be much more posts about it)).
I use Hugo basically all the time.

What I like very much about Hugo, is the fact that it is distributed in a single binary (since it is written in Go).
This makes it portable across devices.
Hence, if you have a binary for Windows, Linux, MacOS and even one compiled for arm64 CPU's, you can use it basically on all of your devices, without installation.
It just works, even on my Android device!

Last but not least, Hugo is extremely easy to use and basically explains itself.
Yet at the same time, you can really do a lot with it (by the way [this website](#) is build fully using Hugo).

## Using a theme for appropriate PDF styling

It is very easy to have a Markdown file rendered as HTML, but the problem is that the styling is wrong for a document, which will be outputted as a pdf.

Basically the text is way to large and the borders are way off, for a A4 pdf document.

Fortunately, I have thrown together [a very simple theme](https://github.com/martinkaptein/hugo-formatting-theme) for Hugo, that presents just the right styling.
This theme can be found on [this Github repository](https://github.com/martinkaptein/hugo-formatting-theme).

### Installation and usage

The theme installs right as any other Hugo theme:

(in your hugo site directory)

```
cd themes
git clone https://github.com/martinkaptein/hugo-formatting-theme.git
```

Add `theme = "hugo-formatting-theme"` to your config file.

You can add your content into `content/`, but will have to browse, while running `hugo serve` to the right URL manually.

Please make sure to take a look at the [README.md](https://github.com/martinkaptein/hugo-formatting-theme/blob/master/README.md) in the github repo for additional notes.

### Different CSS stylings

This theme includes two different stylings, which are referenced to in `themes/hugo-formatting-theme/layouts/index.html`. 

By default you have `<link rel="stylesheet" type="text/css" href="/css/custom.css">`, which produces in my opinion the best result.
The other option is `<link rel="stylesheet" type="text/css" href="/css/styling.css">`. 

In order to switch you will have to manually edit the `layouts/index.html` file, but a parameter will be added in the near future.

### Examples

Here are some examples of pdf outputs with different stylings using the `hugo-formatting-theme` theme and Hugo.

The outputs are already pdf documents.

![custom css styling hugo pdf output](/images/blog/custom-css-hugo-styling.jpg)

*custom css styling hugo pdf output*

![other styling option](/images/blog/styling-css-hugo-styling.jpg)

*other styling option*

## Saving the webpage as pdf

Now that we have rendered a nice HTML page using Hugo, we need to export it as a pdf document (or any other type of document, eg.docx for that matter).

At the time of writing Hugo does not have a pdf output build in.
Hence, we will use our Browser to do that.

In my experience, the best pdf output comes with Chrome (or Chromium) as it allows you to set options like styling.

However, at this point, styling should not be a problem, and the pdf output function of Firefox (or any other Browser) should work just fine.

Hence, we will need additional software, but who knows, maybe this functionality will be added to Hugo at some point in the future.

An other option is to use the [wkhtmltopdf](https://wkhtmltopdf.org/) tool, in order to not leave the Command Line Interface. In my case this tool works perfectly as well!

# Conclusion

This conversion pipeline totally works, but is not as flexible as latex or r markdown.
However, on the other side it is much, much more lightweight and is basically portable.
Additionally to Hugo it is possible to use a portable version of Firefox.

If you would like to see, how to accomlish a comparable result with pandoc, check out [this post](../markdown-to-pdf-without-latex/).
