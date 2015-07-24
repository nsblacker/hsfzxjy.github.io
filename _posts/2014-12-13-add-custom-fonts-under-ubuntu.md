---
layout: post
title: Ubuntu加入自己的字体
permalink: /add-custom-fonts-under-ubuntu/
date: 2014-12-13T07:50:34.000Z
categories:
  - Ubuntu
tags:
  - ubuntu
  - 字体
status: publish
type: post
published: true
---

假设字体文件夹为：`～/Fonts`。执行：

```sh
sudo mkdir -p /usr/share/fonts/myFonts
sudo cp ~/Fonts/*.ttf /usr/share/fonts/myFonts/
sudo chmod 644 /usr/share/fonts/myFonts/*.ttf
cd /usr/share/fonts/winFonts/
sudo mkfontscale  #创建雅黑字体的fonts.scale文件，它用来控制字体旋转缩放
sudo mkfontdir    #创建雅黑字体的fonts.dir文件，它用来控制字体粗斜体产生
sudo fc-cache -fv #建立字体缓存信息，也就是让系统认识雅黑
```
