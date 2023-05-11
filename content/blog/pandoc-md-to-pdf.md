---
title: "Pandoc converting markdown to pdf without LaTeX"
date: 2019-12-26T20:08:17+01:00
lastmod: 2020-01-05T15:08:17+01:00
draft: false
categories:
  - Software
tags:
  - setup
  - writing
  - pandoc
  - markdown
  - pdf
  - converting
slug: markdown-to-pdf-without-latex 
comments: true
description: "Converting markdown to beautifully formatted pdf in the most lightweight way possible, without LaTeX or R. The only thing we will require is pandoc, wkhtmltopdf and one css file. This is the most portable writing setup."
authors: ["martinkaptein"]
cat:
  - technology
---


# Converting Markdown to beautiful pdf without LaTeX 

In this post, I will tell about my journey of attempting to find a lightweight and portable markdown writing setup, that will allow me to produce beautifully formatted pdf documents.

## What I was searching for

I was searching for a lightweight way to convert markdown to pdf, whilst making it look fine, for example when sending someone a paper.

Of course, I wanted to use my favourite text editor (vim) so basically it was clear to me, that the solution would lie somewhere in the direction of LaTeX and Markdown.
It was not my plan to write a PhD thesis or something in that direction, but rather have something to quickly and easily format assignments, in the ideal case even something portable.

Of course, Markdown was the first thing that came to mind, as I am already very familiar with it (all of the text on this website is written in Markdown).
Naturally, I thought whether it was possible to generate a pdf directly from Markdown. For example it shouldn't be too difficult to use [Hugo](https://gohugo.io/) to render a nice page and then save it to pdf (by the way, this website uses Hugo, and I am very satisfied with it).

However, that seemed not a very good idea, seeing as how this method in not efficient at all.

So I continued looking. 

### LaTeX

Very quickly I stumbled across LaTeX, which I immediately liked a lot. From this point on I will probably use it for all bigger "professional" projects.

In my scenario, which I have outlined earlier, however, LaTeX will be a bit of an overkill.

#### Why LaTeX is for different purposes

LaTeX is really amazing, but for quickly writing and printing out reasonably-nice looking documents it is really overkill.
In order to compile LaTeX documents, one needs the full distribution of LaTeX which can quickly weight several gigabytes.
And of course it is far from being portable.

### Pandoc to the rescue!

Then I stumbled upon an amazing tool called [Pandoc](https://pandoc.org/). Basically it can convert any text file into whatever one desires (of course it has also its limitations, but that's not a problem for us).

Also, this tool is reasonably lightweight and portable, which is exactly what I am looking for.

## Pandoc markdown to pdf without LaTeX 

Pandoc can indeed convert markdown to pdf, but it is not that simple. In order to do that, Pandoc needs a so-called pdf-engine, in order to apply styling etc..

By default Pandoc will attempt to use a LaTeX engine (`pdflatex`) which requires, sadly, but very logically, the whole LaTeX distribution installed.

Then I noticed on the [Pandoc manual site](https://pandoc.org/MANUAL.html), that it also allows `wkhtmltopdf` to be used as the pdf-engine. [wkhtmltopdf](https://wkhtmltopdf.org/) is a program that allows for a website to be converted to pdf.
Initially, when I wanted to use Hugo as a pdf generator I have stumbled upon it (as Firefox has a very limited save-to-pdf functionality (in contrast to Chrome) sadly).

Hence, when we run pandoc with wkhtmltopdf it indeed works but the output is very basic.
 
### Pandoc pdf styling without LaTeX

Now, that we are basically dealing with a website, the styling can be accomplished with `css`. One amazing user has [published on github a very good css file for styling pdf's from pandoc and wkhtmltopdf](https://gist.github.com/killercup/5917178). I am not sure about the license bound to this css file, so I will just link to the [github gist thread](https://gist.github.com/killercup/5917178) instead.

#### Build command

Hence, for this process we need only `wkhtmltopdf` and `pandoc` to be installed.

The build command looks something like this:

```
pandoc -t html5 --css custom.css test.md -o file.pdf -s --pdf-engine=wkhtmltopdf
```

The `custom.css` file designates the css snippet, that I have mentioned above, `test.md` is the input and `file.pdf` the output.
By the way, the path to `wkhtmltopdf` can also be a relative one, if you are running this on a portable setup.

You can even add a simple table of contents by adding the `--toc` flag to the command.

Basically, what we are doing is first converting the markdown file to html using some css styling with `pandoc`, and afterwards saving it to pdf through `wkhtmltopdf`.
Funnily enough, things like citations work just fine!

## Shortcomings

Of course this method has many shortcomings. For example adding formulas would be very difficult, and would need to be solved with javascript or css.
Moreover, since html has no "concept" of pages (in the traditional document sense), you can't really control what appears on each page.

Using this method it would be a pain to create for example title pages or slides for presentations.

## Conclusion

Of course, this method is not supposed to 'compete' with LaTeX or R Markdown. This is just a very simple and lightweight way to produce simple written documents that look good.

But if you need a simple and "bloat-free" (meme joke) way of creating pdf documents this might very well be it. No one will be replacing the monsters of LaTeX, R Markdown and others any time soon.
