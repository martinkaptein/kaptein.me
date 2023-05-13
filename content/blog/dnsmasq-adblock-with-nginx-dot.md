---
title: "Selfhosted Dnsmasq adblocker with Nginx DoT server"
date: 2023-05-12T16:02:40+02:00
draft: false
# write a good description
description: "Setting up a selfhosted instance of Dnsmasq for adblocking, privacy and security reasons. We will also setup a DNS over TLS server using Nginx."
cat:
  - technology
  - linux
  - selfhosting
---

## Introduction

In this post I would like to share some experiences regarding hosting my own DNS Adblock Server on a Debian VPS.
The initial motivation was to use a custom DNS for adblocking on all devices, as well as for privacy reasons, as some telemetry domains of any Operating System or Platform can easily be blocked that way.

On this page we will go over a **Dnsmasq** configuration and setup.
We will also setup a DNS over TLS (DoT) server with my webserver of choice, **Nginx**.
This is not strictly necessary, but some clients (looking iOS) prefer a DoT/DoH server.
Hence you can skip the DoT Part, and later configure your client with your IP address.

## Dnsmasq setup

Since my VPS is running Debian, the whole article will be based on the assumption of running Linux.
The steps for other Linux Distributions will be very similar, and the steps for Ubuntu will likely be the same.

First of all, you will need to install Dnsmasq through the package manager of your choice:

`apt install dnsmasq`

After that we will need to do some initial easy configuration.
Find out the interface using `ip address`.
Here we will assume that the interface is `eth0`.

Now, edit with your favourite Text Editor `/etc/dnsmasq`.
In this file uncomment and set the `interface=eth0` (or whatever you have noted earlier).
Also, uncomment `domain-needed`, remove the leading `#`.
Take a note of the default port Dnsmasq will be running on, you don't have to change anything.
Usually it's port 53.

Head over to `/etc/resolv.conf` and check your (default) nameserver.
This is the nameserver your request will be forwarded to.
You can set it to any public DNS resolver, like `8.8.8.8`.
Usually there should already be a value and you don't have to neccessarily change it.

### Dnsmasq Adblocking

For adblocking we have several possibilities at this point.
You could get one of these giant hosts file, like the [StevenBlack host file](https://github.com/StevenBlack/hosts).
Dnsmasq should use them.
However this method doesn't work very reliably, because the formatting of the host file can cause Dnsmasq to ignore it, and forward the requests to the default resolver, thus not blocking.

A much more reliable solution is to setup a file inside `/etc/dnsmasq.d/custom.conf`.
This file can contain all domains you would like to block in the following form:

```
address=/dit.whatsapp.net/0.0.0.0
address=/google-analytics.com/0.0.0.0
```

The advantage of this method is that it works with wildcard domains (e.g. `*.apple.com`).
This way you can block a lot of domains with just a few lines.

You can also convert a giant host file into dnsmasq format with a command like this:

```
wget -O- https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts | awk '$1 == "0.0.0.0" { print "address=/"$2"/0.0.0.0/"}' > /etc/dnsmasq.d/malware.conf
```

However, when you restart the Dnsmasq server later you will need to watch out for errors, and in some situations fix them manually.
Dnsmasq can be picky about some of the domains in this list.

Dnsmasq automatically picks up files located inside `/etc/dnsmasq.d/*` and uses them.
After every change to either `/etc/hosts` or `*.conf` you have to restart the Dnsmasq service for the changes to take effect:

```
systemctl restart dnsmasq
```

In essence you can already now point your client to the IP Address (IPv4 / IPv6) and use your own custom selfhosted DNS Adblock service.

However, some clients also prefer DNS over TLS, so in the next section we will take a look at how to setup that.

## DNS over TLS (DoT)

In the following we will take a look at a very minimal DoT setup using nginx, which is the webserver of my choice.

### Nginx DoT setup with Dnsmasq

This assumes that you are already a little bit familiar with how Nginx works.
Create a new directory, which will contain our nginx config:

```
mkdir /etc/nginx/streams/
```

Inside it create the following config with your favourite Text Editor:

```
upstream dnsname {
        server    127.0.0.1:53;
}

server {
        listen 853 ssl;
        ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem; # managed by Certbot

        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

        proxy_pass dnsname;

}
```

You can see that this assumes that you already have a domain, and a SSL certificate created for it.
If you already have a website running with nginx you don't need to have an extra subdomain.
You can just reuse your existing certbot certificate.
In line 2 in the config above you see that we are using localhost on port 53, the port we have noted earlier, as it is the default port for Dnsmasq.

The last thing we have to do now is to tell Nginx about our new config directory.
Include this block in `/etc/nginx/nginx.conf`:

```
stream {
        include /etc/nginx/streams/*;
}
```

Now restart Nginx and we are already done!

```
systemctl restart nginx
```

## Client setup

Last but not least I would like to provide a few notes about how to configure DNS on various devices/clients.

### Linux

On Linux it is very simple:

Go to `/etc/resolv.conf` and set:

```
nameserver your.public.ipv4
nameserver your.public.ipv6 (optional)
```

### MacOS

On MacOS you can use Terminal:

```
sudo networksetup -listallnetworkservices
sudo networksetup -setdnsservers Wi-Fi ip.adr.here.0 optional.secondary.0.0
```

If you need to reset it to DHCP run this command:

```
networksetup -setdnsservers Wi-Fi empty
```

Verify your DNS server with this command:

```
networksetup -getdnsservers Wi-Fi
```

### iOS

Unsurprisingly iOS is a little bit annoying.
It lets you set custom DNS for WiFi but not for Cellular.

To work around it you can create a custom profile [using this website](https://dns.notjakob.com/tool.html).
There you can set the IP addresses and most importantly set the DoT domain, which we have setup earlier.
