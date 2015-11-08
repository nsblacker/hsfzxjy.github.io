---
layout: post
title: Ubuntu下删除不完整的包
date: 2014-12-13T05:41:10.000Z
categories:
  - Ubuntu
tags:
  - ubuntu
status: publish
type: post
published: true
---

答案来自[StackOverflow](http://stackoverflow.com/questions/27455626/how-to-remove-an-incomplete-package-by-using-apt-get):

```sh
sudo dpkg --remove --force-remove-reinstreq <your package name>
```
