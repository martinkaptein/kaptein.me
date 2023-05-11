---
title: "Introduction to Crypto in 2021"
date: 2021-04-20T11:04:57+01:00
lastmod: 2021-04-20T11:04:57+01:00
draft: false
metaImage: /images/blog/btc-wallet.jpeg
description: "Easy introduction into how cryptocurrencies work, and a easy and concise way. All cryptocurrencies share very similar underlying principles in regards to their ledger blockchain, wallets addresses and much more. Also, I will feature some advantages and disadvantages of crypto currencies."
slug: crypto-easy-introduction-2021
keywords:
  - introduction
  - cryptocurrencies
  - opinion
  - easy
  - blockchain
  - wallet
  - address
cat:
  - technology
  - crypto
  - introduction
---

## Easy Introduction to the way Cryptocurrencies work

In this blog post my goal is to explain how **cryptocurrencies** generally work, in an easy and concise way.
We will not be diving into too many technical details.
This blog post in meant for enthusiast who just want to have an overview of how crypto works.

**Disclaimer**

This blog post is not meant as financial advise, and just features my **personal opinions**.
I will not mention and talk about social, political or financial ramifications, but instead will purely focus on a technical overview of the fascinating technology involved in the world of cryptocurrencies.

### Intro

Probably, you have already heard of *Bitcoin* before.
It is important to mention that there are hundreds (if not thousands) cryptocurrencies like that available, some with slightly different technical features and some not.
Important to understand is that all of them share very similar underlying principles, which shall be outlined in this post.

### Basic principles of cryptocurrencies

The basic of all cryptocurrencies in quite simple in essence:
Most of them provide a ledger (or a **list** in other words) of all transactions happening, and all historic transactions, going back to the point the (any) cryptocurrency was made.
Very important to understand, that this list is, in most cases of cryptocurrencies, **completely public**.
This means that **everyone** can have a look at this list, which we call *Blockchain*, see how much balance each address has, how many 'coins' have been sent etc..

The core principle of every cryptocurrency is to provide a system, with to guarantee that all parties 'agree' on a single true list/ledger/blockchain.
Currently, there are two mechanics to enforce this system, one by **mining**, which involves solving a lot of very difficult math, to guarantee, that a 'bad actor' cannot 'outrun' the *true* list.
The other system, which different cryptocurrencies use is **Proof of Stake**.
In it the users of the cryptocurrency provide a investment of their own 'coins' (like investors or shareholders).

With both systems are mechanics which **reward** the *miners* or *stakers*.

Again, all of this is done just to guarantee that everyone uses the same list of true transactions and agrees on it ('consensus').

### How crypto wallets and addresses work

Let's have a look now at how a wallet works.
Again, in this post I will be simplifying a lot.

Essentially, a cryptocurrency wallet (like a Bitcoin wallet), consist of (basically) **two** very long numbers, or **keys**.
A public and a private key.
These two keys are linked mathematically together, but it is not possible to calculate the private key when you have only the public key. 

Essentially, the **public key** *is* the wallet address.
When you have a balance, eg. `n BTC` it is associated with your wallet, i.e. your public key.

The private key, which **belongs** to the public key, is used as a proof that you can make spendings from your wallet.
When you want to transfer money away from your wallet, you create a **signature** with your private key, to prove that you are indeed the owner of your wallet.

This is why it is very important to keep the private key private!

In all of this is lots of math involved, which is called *cryptography*.
That is why we are talking about **Crypto** currencies.

#### Getting a crypto wallet

When you want to get a cryptocurrency wallet, you don't need to create an account or anything whatsoever.
Essentially, to **create a wallet** you just need to generate a key-pair (public and private key), which is done automatically by your wallet software, according to the specifications (algorithm) of the crypto currency which you chose.

These keys are generated, basically, randomly, and there almost infinite (not *actually* infinite, just for the sake of the argument) possibilities available.
This why you can easily **generate** thousands of wallets if you would want to.
And statistically it would be **very** unlikely, that you would have the same keys as someone else.

Here is an example cryptographic address (public key), which you could theoretically send money to (this is actually my bitcoin address, so it would be very much appreciated).
```
14cCkoxS3JHFfczMj3zYe2BVrZ8TfgVqaF
```

And, because it is in most cases easier to just scan a QR code with your phone wallet, here is the same address in QR code form:

![Bitcoin address as QR code](/images/blog/btc-wallet.jpeg)

*Bitcoin address as QR code*

Many wallets also provide a certain amount (12,24,48) of backups words, a **backup phrase**, in order to recover and back up your wallet more easily (as opposed to writing down the long and complicated secret key).
This is just an agreed-upon system, which can get the private and public key from those words.
The underlying system and principles stay the same.

Again, because the blockchain is public, you could easily take my public address and look up my balance on it!
This is important to keep in mind.

Of course, there are more technical intricacies, such as secondary address and privacy coins.
If there is interest for that (feel free to contact me for feedback), I will write a more detailed follow-up post.

### Advantages of Crypto Currencies

Let's have first a short overview of some advantages that crypto currencies provide.

Crypto currencies (at least most of them), are decentral, that means there is not one instance, which can control the supply and demand, block transactions etc.
Moreover, crypto currencies have a very clear and transparent system of their workings, meaning everyone can go ahead and personally make sure, the software does what it should.
Basically, you don't have to trust crypto currencies, because their inner way of workings makes it virtually impossible to be a 'bad actor'.

Trustless security in IT is the best kind of security.

Also, cryptocurrencies are much more resilient to censorship, crashes and being disabled by a bad actor.
As long as there are a few computers running the crypto software, and are connected to the internet, everything will continue to work fine!

Last but not least, as no one **controls** crypto currencies, their are much more stable in terms of inflation.

### Disadvantages of crypto currencies

For the sake of objectivity, let me mention a few disadvantages of crypto currencies as well.

First of all, there is the big problem of privacy.
As we have discovered, all the transactions are public by design, which makes it incredibly easy to trace all transactions.
However, there are *privacy coins* which mitigate a lot of these problems.
I trust you will discover them by yourself.

Furthermore, there are possibilities of uneven coin distribution, as people who acquire a crypto currency early, have a very big advantage, as its value is still very low.
For this are also technical mechanics to mitigate it, such as controlling how much crypto is being 'released' at a time (*mined*).
Of course, this is not controlled centrally, but rather *by design* (in the specifications of the algorithm of the cryptocurrency).

Last but not least, for many crypto currencies (at the moment of writing) exist the problems, that transaction cost for smaller transactions are still very high (which has something to do with rewarding miners as previously mentioned).

## Summary

This was just a very short overview of the world of crypto currencies, and how they work.
I did not mention too much technical details, as the goal of this post was to function as an introduction for beginners.
Of course there are many different crypto's available, which all aim to solve slightly different problems.

Some crypto currencies solve almost all of the problems which I have mentioned (see my contact page for an example of a crypto currency which I would definitely recommend).
