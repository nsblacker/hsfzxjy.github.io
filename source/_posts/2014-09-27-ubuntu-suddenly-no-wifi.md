---
layout: post
title: 关于Ubuntu突然无法连接Wifi的解决方案
date: 2014-09-27 18:41:31.000000000 +08:00
categories:
- 随手记
tags:
- ubuntu
---

> 事实上我也不知道发生了什么，大概是几天前插了“小度Wifi”的缘故。没有任何征兆地，Wifi就用不了了。 其实我也不知道原理，大概是某个驱动被刷掉了。

下面是从网上找来的答案：

```sh
sudo apt-get install wicd-daemon
```

做个记录。
