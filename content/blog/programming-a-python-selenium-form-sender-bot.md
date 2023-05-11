---
title: "An introduction to Browser Automation - Programming a form sender bot in Python using Selenium"
date: 2018-07-09
lastmod: 2019-09-21
draft: false
categories:
  - Programming
tags:
  - Python
  - developement
  - selenium
  - form sender
  - bot
  - browser automation
slug: programming-a-python-selenium-form-sender-bot
comments: true
description: "An tutorial for Browser Automation. In this tutorial we will be programming a very simple bot in Python using Selenium to send forms."
authors: ["martinkaptein"]
cat:
  - technology
---


### Short introduction

In this tutorial we are going to have a little bit of fun. Recently my University fell prone to a Scam attack, in which a scammer build a similarly looking website (to our University) in order to gain access to private data. The link to this fake scammer website was send via a mailing list to all of the students, with a warning, that everyone should log in, otherwise their account was to be deleted. 

Update: The website since has long be taken down, but the steps outlined in this post still are absolutely valid.

I saw this as an opportunity to program a very simple automated browser spam bot, which will endlessly spam the input form with, well, let’s just say *an input*.
The scammer didn’t see it coming:)

## Installation and Getting everything ready

Brilliant tools for simple (and complex) Browser automation are the synergy of [Python](https://www.python.org/) and [Selenium](http://selenium-python.readthedocs.io/).

First of all, make sure you have **Python** (I have Python 2.7.10) installed. Also, make sure to install **Selenium**:

`sudo pip install selenium` 

After that, we need to install the driver, that will allow Selenium to talk and use your Browser. You can find the drivers [on the official doc page of Selenium](http://selenium-python.readthedocs.io/installation.html).

In this post we will be using **Chrome on MacOS**, but the steps for other browsers on other platform are very similar.

Unpack the downloaded .zip file and place the `chromedriver` file in `usr/local/bin/`:

The command will look like this:
```
cp Downloads/chromedriver_mac64/chromedriver usr/local/bin/
```

Now, we get to the coding part:)

## Programming the Browser Automation bot in Python and Selenium

Create a new file called `whatever.py`:

`touch whatever.py`

In the file start by importing the **webdriver** module:

`from selenium import webdriver`

Now, lets define the driver var:

```
driver = webdriver.Chrome()
```
Now we can get to the meat!

Let’s open the webpage that we need to spam:

```
driver.implicitly_wait(10)
driver.get('https://artez-nl.weebly.com/')
```

We use `implicitly_wait` in order to make sure that the website has loaded, `get` gets the website (duh).

Now, we need to find the elements of the form, we need to fill in. Let’s open the normal browser, navigate to the target page of the scammer and view the source code.

In my case, the form elements look like this:

![website html source code](/images/blog/target-website-source.jpg)

*website html source code*

We can clearly see that there are 3 text fields that we will need to fill out:

- Mail
- Password
- Confirm password

Each fields have (somewhat cryptic) input id’s, which we are going to use in order to be identified from the script:

For this, we use `find_element_by_id`.

```
elementMail = driver.find_element_by_id("input-512150653825676534")
elementPassword = driver.find_element_by_id("input-986570961994892506")
elementPasswordConfirm = driver.find_element_by_id("input-147369398988478792")
```

Ok, now we have to fill the input fields:

```
elementMail.send_keys("TotallyLegitMail@mail.ru")
elementPassword.send_keys("MyTotallySecurePassword")
elementPasswordConfirm.send_keys("MyTotallySecurePassword")
```

The only thing left to do now, is to send the form: In this case we are going to *find* the submit button by class name and then click it:
```
driver.find_element_by_class_name("wsite-button-inner").click()
```

And.. This is it!

Basically it is an incredibly simple process but you can make it as complicated as you want.

Since this is an browser automated spam bot, lets put everything in a never-ending while loop and add a counter.

In the end, the whole file will look like this:

```
from selenium import webdriver


driver = webdriver.Chrome()
counter = 0

while True:
    counter += 1
    driver.implicitly_wait(10)
    driver.get('https://artez-nl.weebly.com/')

    # find elements
    elementMail = driver.find_element_by_id("input-512150653825676534")
    elementPassword = driver.find_element_by_id("input-986570961994892506")
    elementPasswordConfirm = driver.find_element_by_id("input-147369398988478792")
    
    # enter text
    elementMail.send_keys("TotallyLegitMail@mail.ru")
    elementPassword.send_keys("MyTotallySecurePassword")
    elementPasswordConfirm.send_keys("MyTotallySecurePassword")

    # send form

    driver.find_element_by_class_name("wsite-button-inner").click()

    print counter
```

## Conclusion

Working with Python and Selenium is truly a joy, there are really a lot of possibilities!

This here is a very simple example, feel free to make it as complicated as you want. 

Perhaps throw in some **Deep Learning** with **Keras** in order to solve captcha’s.

But we’ll get there eventually:)


