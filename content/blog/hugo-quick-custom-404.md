---
title: "Hugo - Custom 404 page from content markdown file"
date: 2020-06-04T12:39:38+02:00
draft: false
description: "How to make a custom 404 page in Hugo just from a content markdown file. This approach will not require changing the theme layout template and is very easy."
tags:
  - hugo
  - custom 404 page
  - tutorial
  - templates 
  - front matter
  - markdown
  - content
categories:
  - hugo
slug: hugo-custom-404-page-from-content-markdown
comments: true
cat:
  - technology
---


# Making a custom 404 page from a content markdown file in Hugo

In this blog post we will be taking a look, at how to easily make a custom 404 page without changing the layout templates in Hugo.
We will be able to build this page like any other regular markdown content file in Hugo by just adding an additional parameter in the front matter of our file.

## 404 page format for static site generators

Static site generators usually output a `404.html` file in the root directory of their output.
The server subsequentely is configured to "serve" this file, when a page is not found.
This post does not deal with the server configuration, but if you need help with that part, you can consult [this page about server 404 redirect configuration](https://gohugo.io/templates/404/#automatic-loading).

Various static hosting providers like *github* or *netlify* already come pre-configured for this, so you won't have to adjust anything.
If in doubt, please consult your hosting provider.

## Content markdown file for custom Hugo 404 page

First of all, start by just creating a new markdown file in your `content/`or arbitrary directory, where you keep your pages (=not blog posts):

`hugo new content/404.md`

For easy usage we will name this file `404.md`, but it can have any name, actually.

You can edit this file like you would any other markdown content file, add links (probably adding links to the homepage is a good idea).
Of course, the main menu of the site will appear on this page as well.

As far as hugo is concerned, this is just a 'regular' page.

## Front matter adjustments and setting the url parameter

In this part comes the magic of hugo: Usually, in the content front matter, you can provide a post/page slug, but in this case we will be using the `url` parameter.
With this parameter we will tell hugo, that we want this page to be named `404.html` specifically (without having to set [ugly urls](https://gohugo.io/content-management/urls/#ugly-urls)):

`url: 404.html`

Now, hugo will automatically add this page to the output (in the root folder) and name it `404.html` - exactly what we want.

### Markdown file example

Here is the example how the end result may look like:

```
---
title: "404 Page not found"
draft: false
description: "404 error page not found."
url: 404.html
comments: false
---

# 404 Error

## This page has not been found

You are advised to [head back home here](/).
```

Of course, like in any regular file, you can add any front matter parameters like on a regular page, this is entirely up to you.

## Things to keep in mind

Here are just some various things to keep in mind.

### Hugo local server 404 testing

Keep in mind, that (until now) the local `hugo serve` command will not automatically redirect to the 404 page, when you navigate to a non-existent page on your site.
In order to test this page (locally) you will need to navigate manually to (by default):
```
http://localhost:1313/404.html
```

### The usual approach of constructing 404 pages in Hugo

The usual approach, which is also recommended by the [Hugo 404 docs](https://gohugo.io/templates/404/) is to create a separate layout file inside `layouts/`.
This approach provides you with much more fine-grained control over your page: You could use different meta tags, menu layout and even a totally different design.
But for those who just want to quickly generate a custom 404 page in Hugo, the approach of using the `url` parameter in the front matter is much easier, and does not require the user to dig deep into Hugo template construction.

