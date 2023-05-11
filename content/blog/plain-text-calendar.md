---
title: "Events txt plain text calendar solution"
date: 2021-05-16T10:34:32+02:00
lastmod: 2021-05-16T10:34:32+02:00
draft: false
description: "Plain text full-featured calendar solution, which is portable and works on all platforms. Events txt allows for easy import and exporting and is completely open source. It is very easy to use and I use it all the time."
metaImage: /images/blog/events-txt-plain-text-cal.jpg
keywords:
  - plain text calendar
  - calendar
  - txt
  - events txt
  - script
  - easy
  - open source
  - vim
  - multiplatform
  - portable
cat:
  - technology
---

## Plain text calendar 

*16 May 2021*

For a long time a was searching for a calendar solution, which would be as portable and self-sufficient as possible.
Of course this meant I had to go the plain-text route.

![Plain text calendar Events txt](/images/blog/events-txt-plain-text-cal.jpg)

*Plain text calendar Events txt*

For a while I tried org mode, but as I haven't mastered Emacs (yet?) using org mode didn't make a lot of sense.
Also, while org mode itself is plain-text, you still had to rely on an external framework (like Emacs) to have a clear overview of upcoming events, and make easy date selection when creating a new event.
That said, I was impressed to find very high quality org mode apps for various devices.

Hence, I decided to come up with my own solution, which would suit my own needs, and, as it is completely free and open source, also possibly needs of other people.
I wanted to have full control over my calendar (backups, importing, exporting etc.), hence the ical format was not an option, and it should work on as many different devices as possible, basically on **every device**.
This is what I came up with:

## Introducing Events.txt

The *solution* I have created is named Events.txt.
It is basically just a text file containing a calendar for a predefined number of years ahead.

In order to create and maintain (I will talk about reoccurring events later), I wrote two Python scripts, which are in [the Events.txt GitHub repository](https://github.com/martinkaptein/events.txt).
One script (make.py) creates the file, and the other (maintain.py) can performing maintaining operations on the file.

By the way, the idea for the format of Events.txt, was inspired [by this post about plain file task and calendar management](https://danlucraft.com/blog/2008/04/plain-text-organizer/).

It is very easy and clear to use Events.txt on any device that is capable of opening a text file.
Also search operation in this file (like jumping to next events, searching for a date etc.) are made in a very comfortable way, thanks to the Events.txt format.

Moreover, advanced calendar features such as regularly repeating events (such as birthdays) are supported as well.
Let's have a closer look at it!

### Events txt plain text calendar format

The basic Events txt plain text calendar looks in the following way.
Keep in mind, that the user is free to change the way dates appear, first days of weeks, etc. in the source of the Python script.

```
.
.
.
May
01/05/2022 Sun | + some Event
______
02/05/2022 Mon |
03/05/2022 Tue |
04/05/2022 Wed | + 1200 May the force be with you
+ 1230 More events added on new lines to improve readability
+ 1300 May the force stay with you
+ 1800 Hopefully it is still there
05/05/2022 Thu |
06/05/2022 Fri | + 0600 Is the force stil there?
.
.
.
etc.
#repeatingYearly
04/05 - 1200 May the force be with you (this is an event (like a birthday) which repeats every year)
```

This is the format you get, when you just run the `make.py` script.

The notation of time and dates, and adding of new events really explains itself.
New events start with a plus sign, then the time in 24h format (12h format possible as well).
Multiple events on one day, just use different lines, this way the file stays very well readable.

If there is an event which repeats every year, it is added at the bottom of the file, under `#repeatingYearly`, in the format `day/month - time EventDescription`.
Then, when you use the `maintain.py` script on it, all the dates are automatically added for each year.

The calendar is made in such a way, that you don't need to use the Python scripts often.
This is why to use this calendar solution you *really* just need a text editor, which should work on every device, even very old ones.

### Usage

If you have access to a UNIX-style Terminal, and have git and python installed, you can create a fresh Events txt calendar file like this:

```
git clone https://github.com/martinkaptein/Events.txt.git
cd Events.txt
python make.py > Events.txt
```

By default the `make.py` script prints its output as standard output, that's why we redirect it with the `>` sign to a file.
Of course, the file can have a different name as well.

If you have two python installations you might have to substitute `python` for `python3`.
If you want to make adjustments to how the calendar looks like, you will have to edit the well-documented python code (at least at the moment of writing).

In order to fill-up your existing calendar with more days, and 'take care' of repeating events such as birthdays, you are invited to use the `maintain.py` script.
You can just run it with:

```
python maintain.py
```

**Note:** For now it expects your Events.txt file to be in the same folder and have that exact name, otherwise it will throw an error.

Of course, after you are done you are free to copy/transfer your calendar to any device you please (as long as it has a text editor, and can read and write .txt files).

### Source

Again, the source code for Events.txt can be [found here on GitHub](https://github.com/martinkaptein/events.txt).
There, you will find the two python scripts.

### Usage examples and scenarios of plain text calendar

This solution makes many calendar operations and usage scenarios much easier.
For example, it is very easy to scroll through events, make queries (using your favourite text editors find or find-replace function).

Another advantage, is that this calendar solution is completely future-proof.
You can easy import and export events, and parse the file easily with any programming language, in order to do more complex things with it, which you have all freedom for.
Can you do that with your Calendar?!:)
In this calendar you are really in control over your future (both figuratively and literally).

Last but not least, this calendar is actually very easy to use, as you can really quickly write down events.
At least, I am much quicker with it than with the default Android or iOS calendar.

It is easy to make this calendar accessibility-friendly, think visually impaired, audio functions etc..

## It works

This is not only a proof-of-concept, but rather a really workable solution.
At this point I have used this calendar for over a year very actively, and I am definitely not going back.

On the computer I use it with vim, on my mobile devices I just use an open source text editor.
Actually, if you have an editor which remembers your last position in the text file, you don't even need to remove old events (from the past) from the file.
It is very easy to synchronize, make backups, diffs etc..

Also, you can easily integrate your to-do lists and notes into Events.txt if you like to.
Then you really have everything in a single text file!
