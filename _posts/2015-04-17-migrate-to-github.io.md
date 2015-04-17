---
published: true
layout: post
permalink: /migrate-to-github/
title: 博客迁移至Github.io
---
###为什么迁出？

话说**SinaAppEngine**真是越来越不像话了：在没有征得我们开发者的同意的情况下擅自把应用总数限制调整为5个（整整少了一半！），还口口声声说是作过调查——

> “大约90%开发者只用5个应用就足够了。”

同时，增加配额的钱还那么贵，实在担负不起的我只好精简应用数目，以防未来某天应用数不够用。

###为什么选择Github Pages？
本人爱好程序，习惯以代码的方式来做事——写文章时也不例外。因此，我需要找到一个支持Markdown的博客平台进行迁移。为此，我经历了很长时间的思想斗争——

**新浪、网易 等国内博客平台？**

果断否决。这些平台都是面向大众的，只提供富文本编辑器，效率捉急。

**博客园？“程序员的网上家园”，总会好一些吧？**

虽说最近博客园推出了Markdown编辑器，一切似乎很美好。但是——它——没有即时预览的功能！！这么重要的东西都不加上，写作时就像浑水中摸鱼一样，别提多不爽了。再说了，在博客园上聚集的多是些常工作于Windows平台下的程序员，在“信仰”方面有些合不来（别打我～～）。思考再三，还是否决了。

而事实上，比起公共博客平台，我还是比较喜欢个人博客。一来逼格比较高，可以为将来的交友、面试等活动加分；二来可以随心所欲地自定义样式，使网站完全符合我的Style。

这么一来，似乎就只剩下Github Pages了。

###那么，如何在Github Pages上进行写作？

首先要介绍一下 Github Pages 的架构。先看看 [Github的介绍](https://help.github.com/articles/using-jekyll-with-pages/#using-jekyll)：

> ####Using Jekyll    
> Every GitHub Page is run through Jekyll when you push content to a specially named branch within your repository. For User Pages, use the master branch in your username.github.io repository. For Project Pages, use the gh-pages branch in your project's repository. Because a normal HTML site is also a valid Jekyll site, you don't have to do anything special to keep your standard HTML files unchanged. Jekyll has thorough documentation that covers its features and usage. Simply start committing Jekyll formatted files and you'll be using Jekyll in no time.

可以看得出来，Github Pages使用Jekyll作为后端引擎——这是一个用Ruby写的博客框架。但用户不需要写一行Ruby的代码，只需在名为**<username>.github.io**的项目下面以一定的目录结构放置markdown文件，Jekyll便会自动生成整个站点。

这里需要注意的是，Jekyll生成的站点是**静态的**，也就是说站点的文件是Jekyll编译好之后存放在服务器端的，而不是接到请求之后才去编译站点，因此站点的访问速度是相当快的——这也是它的优点。

---
我被这种机制深深地震惊了：这是一种我从来没见过的写作方式，无论是从方式上，抑或是从形式上。Jekyll 能让你真正专注于写作，而不是其他一些无谓的东西。     

它把一切无关的东西都摒弃了，这才是真正的极简主义。

---
最初的Jekyll站点是没有样式的。为了不重复发明轮子，我决定使用现成的主题。在网上略一搜索便有了收获：[Jekyll Bootstrap](http://jekyllbootstrap.com/)。

Bootstrap是我最常用，也是最欣赏的一个前端框架。因此尽管这个主题仍在开发当中，我还是毫不犹豫地选中了它。    

从 [Github](https://github.com/plusjade/jekyll-bootstrap.git) 上将这个项目 clone 下来，覆盖到hsfzxjy.github.io项目下，理论上，站点就可以运行了。接下来，进行一些样式上的微调就可以了。   

至于评论系统，由于 Github Pages 是静态站点，因此只能使用第三方评论服务。Jekyll 默认的评论服务是Disqus ——一个国外的评论服务站点，但考虑到我在国内，许多人无法使用Facebook，Twitter等社交平台登录评论，我将它替换为了**多说**。具体操作，可以参考 [这里](http://havee.me/internet/2013-07/add-duoshuo-commemt-system-into-jekyll.html)。

Github Pages上的文章只能在本地编辑，因而需要一个趁手的 Markdown 编辑器。在 Ubuntu 环境下我使用的是 **ReText**：

    {% highlight c %}
    sudo apt-get install retext 
    {% endhighlight %}