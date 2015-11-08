---
layout: post
title: Ubuntu下解决apt-get “Hash校验和不符的方案”
date: 2014-11-29 18:26:18.000000000 +08:00
categories:
- Ubuntu
---

各种坑爹，我也不知道为什么：

    sudo gedit etc/apt/apt.conf.d/00aptitude

最后加一行：`Acquire::CompressionTypes::Order "gz";`
