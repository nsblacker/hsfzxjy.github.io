---
title: 如何备份apt-get已安装的软件列表？
layout: post
author: hsfzxjy
categories: ubuntu apt-get
tags: ubuntu apt-get
---

`apt-get`是 ubuntu 下管理软件包的一个工具，实用简单，功能强大。平时若要安装或卸载软件包，只需轻敲一条指令即可。每一台ubuntu上，都安装着数以千百计的软件包——或是内核模块，或是工作、娱乐所需的软件，在它们的支持下，工作着这个开放的操作系统。

但，如果有一天，系统需要被重装——或是无可救药了，抑或是购置了新的设备，问题来了：

> 如何将现有电脑上的软件包迁移至新的系统呢？

很简单。

首先，将原有的软件列表导出：

    sudo dpkg --get-selections  > app-backup-list.lst
    
最好是设置一个定时任务，每隔一段时间就保存一次列表，并且要保存到一个独立的分区。以免某天系统真的坏了。

接下来便是导入了：

    sudo dpkg --set-selections < app-backup-list.lst
    sudo apt-get -y update
    sudo apt-get dselect-upgrade
    
至于软件源的备份，只需将`/etc/apt/sources.list`文件复制过去即可。