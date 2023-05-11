---
title: "Using GPG concise tutorial"
date: 2021-04-08T10:29:00+02:00
lastmod: 2021-04-08T10:29:00+02:00
draft: false
description: "Easy and concise GPG usage tutorial showcasing all the basic functionality of the open source OpenPGP keypair management system. Encrypting and decrypting messages and files easily, importing and exporting keys and various usage scenarios."
slug: using-gpg-tutorial
keywords:
  - GPG
  - OpenPGP
  - GPG management
  - Keypair
  - Encryption
  - Decrypt
  - tutorial
  - easy
  - open source
cat:
  - technology
---

## Getting started with GPG

This article will be dedicated to GPG.
My idea is to provide a very easy but concise tutorial and introduction to GPG, explain the advantages of this system and help with all main commands in order to be able to utilise OpenPGP encryption to its full potential.
In this blog post only the most important commands will be provided to get you started.

### Introduction to GPG and why it is amazing

GPG is preinstalled on most systems, MacOS and Linux in any case.
There are also possibilities to get it on Windows.

GPG is an implementation of the OpenPGP encryption algorithm and system.

Imagine the following scenario: You would like to send a message or file to me, and you want to be sure that only I can read it and no one else (guaranteed).
You could encrypt the file with a password, but then you would have to send the password to me via a secure method.
This opens up the possibility of someone intercepting this password and decrypting your files.

Luckily there is OpenPGP, or **GPG** (how I will call it from now on) to help.
GPG uses a different system to encrypt stuff: In contrast to an encryption password you have two files (or "keys"): A public key and a private key.
Basically you can encrypt a file with the public key but you can only decrypt it only with the private key.
There is a lot of math (cryptography) involved to make this system work, which will not be explained by this article.

But what is important that this aforementioned cryptographic algorithm is public, and can be checked by everyone, to make sure it is secure and it works (which is the advantage of "OpenSource").

This means that you can send a file or message to me, that only I can decrypt, without having to send me a password or anything at all.
You would only need my public key (which is literally open to the whole world), which you can find [on my contact page](/contact/).

Apart from encrypting and decrypting files you can also use GPG to sign files and messages, in order to prove they are from you (and no one else).
Let's have a look how it works, and learn all the basic commands.

### GPG management

#### Creating a Keypair

Before we do anything with GPG we need to initialize a GPG keypair (the aforementioned public and private key).
For this tutorial I will assume that you have GPG installed on your command line, and provide commands to run from the Terminal of your computer.
This is arguably the easiest way to use GPG.

Creating a GPG keypair is very easy with just the following command:

`gpg --full-generate-key`

You will be asked for some information, feel free to enter anything you like.
For ease of use it is best to enter the true information (since you probably intend to publish the public key once we are done).
But strictly speaking this is not necessary.

You will also be asked for a password to secure the private key.
This password is like a secondary defence, and is always required to 'decrypt' your private key, in order to do operations with it (such as decrypting or signing messages).
Please do not lose this password and chose it wisely.

#### Importing and exporting keys

Now that you have created your keypair you will probably want to publish your public key (e.g. on your own website), so someone could send encrypted messages to you.
To export your public key you can use the following command:

`gpg --export --armor yourname@yourmail.com > pubkey.asc`

As the mail address you should use the same address you typed in when you created your key (this is like your user id).

Now you will have a file called `pubkey.asc` in your Terminal working directory.
This file you can safely publish on your website.
You can also open it with a Text Editor and paste the public key somewhere in text form.

Public keys also have fingerprints to verify their integrity.
To get the fingerprint of your public key you can run:

`gpg --list-keys --with-fingerprint`

A bit later in this post we will go over how to export your private key as well, in order to make backups on other devices and don't lose it.

Now let's say you would want to send an encrypted message to me.
First of all you would need to import my public key.
Actually you can use my real key and find it on my contact page or use [the direct link to my public key](/pubkey.asc).

When you have downloaded the key to your Terminal working directory you can run the following command to import it:

`gpg --import pubkey.asc`

Usually you also want to 'trust' my public key.
In order to do that you will have to edit my key.

`gpg --edit-key martin@martinkaptein.com`

Then write `trust` , `<Return>` , `quit` , `<Return>`.

So now that you have imported my public key, you can encrypt something to me.

#### Encrypt and Decrypt using GPG

Alright, now that you have imported and trusted my key, how do you encrypt a file or a message to me?
You can write a message to a `.txt` file or perhaps you have a picture or other file you want to encrypt.

We use the following command to encrypt it:

`gpg --encrypt --armor -r martin@martinkaptein.com yourfile.txt`

In this case I have typed my real mail, you want to substitute the mail address for the address of the public key you have previously imported.

The command above created a new file in your Terminal working directory called `yourfile.txt.asc`.
This file is encrypted now, and you can send it over a (untrusted) mail connection of even publish is openly on a website.
You can send this file as an attachment or open it with any Text Editor and copy the contents of it to a mail message.
Thanks to the `-- armor` parameter it has been converted from binary format to 'normal' text format.
So that's great!

It will be only possible to decrypt this file with my private key.

Now imagine that I have imported your (the Reader) public key on my computer and I reply with a message which is only meant and decryptable by you.
You can save the encrypted file with the `.asc` (or whatever) extension to your working directory and run the following command to decrypt it:

`gpg --decrypt encryptedFile.asc > destination.txt`

Your GPG program will automatically handle all the stuff in the background and ask you for your 'secondary defence' password (which you have set earlier).

And that's it! Now you have the decrypted message from me.

### Storing and managing your GPG keypair on other devices

In this article I only explained how to export your public key.
But what if you want to export your private key in order to make a backup of it, or import it on a different computer.

You can use the following command to export your private key:

`gpg --export-secret-keys --armor yourname@yourmail.com > private.asc`

In your working directory you will have now a file called `private.asc`.
Please handle this file with care as it is your private key.
But it is still secured with your password.

You can transfer it to a different computer (but please do so in a secure way) and import it with the methods described earlier.
Also, if you encrypt and decrypt things often on your android phone, you can use the free app OpenKeychain (also available on Fdroid) to manage your keys, encrypt and decrypt files.

You can also back your private key op in a password manager like the (recommended) KeePassXC password manager.
Your private key can be imported as a file, but you can also open it with any Text Editor and copy the contents (which is basically scrambled text) manually.
But again, please be careful, as it is your private key after all.

This blog post and article did not provide all information on the functionality of GPG (which is really a lot by the way).
But now you know how the basics work, and you will be able to figure out the rest.

Feel free to contact me if you have any remarks, and feel free to encrypt your messages as well.
