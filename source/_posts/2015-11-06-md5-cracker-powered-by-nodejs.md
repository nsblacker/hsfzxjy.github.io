---
layout: post
title: 初试 node.js：MD5 解密网站
categories: 编程 node.js
tags: mongodb node.js express.js
---

## 前言

_有些日子没写技术笔记了。正好今天刚月考完，写篇东西放松一下。_

node.js，IT界的新角，怀揣着用 javascript 称霸前后端的野心。一年前听说这个东西时，我就被其魅力深深地吸引了。尽管从语法上看，js 继承了其父丑陋的风格，无法和我钟爱的 python 相提并论，但人家的性能却是不可小觑的。浏览器脚本起家，天生支持异步编程，时间驱动，完美压榨 CPU 时间，简直让同步的 python 望尘莫及——更何况，还有 Google 大牛精心优化的 V8 引擎，速度快得飞起，完全弥补了其语法上的不足。

早就想学 node.js 了，却一直苦于没有动机。软件工程的学习和其他学科很是不同：如果没有动机，没有实践，仅是读干巴巴的文档，那是很乏味的。在之前的项目中我一直使用 python。在对性能没有过高的要求的情况下，python 是敏捷开发的不二之选。而且在 SAE 支持的三种语言中，我最擅长的便是 python（好吧，其实是其他两种我都不会～～）。学习 node.js，确实没有太急切的需求。

约摸两个星期前吧，@cc 提出了一个新的 idea——在高考后建一个网站，记录同学们毕业后的去向。具体需求尚未确定，但我非常感兴趣。乍一看来，websocket 是必不可少的了，而且对于这类 IO 密集型的网站，MySQL 水土不服，WSGI 模式吃不消。于是我又想到了 node.js——正好趁这个机会，再学一门技术。技多不压身嘛。

于是，在上周我写了个小 [demo](https://github.com/hsfzxjy/md5crack/)，借此透析一下 node.js 及其常见框架。

说了那么多废话，切入正题。

## 需求 & 构思 & 准备

一个小 demo 而已，需求很简洁：

> + **MD5 加密功能** 用户可以输入任意字符串，网站会返回字符串的 MD5 值，同时将原始串和哈希值存入数据库
> + **MD5 解密功能** 用户可以输入一个合法的 MD5 值，网站会检索已知的 MD5 值及其对应的原始字符串，若比对成功则返回原串，否则显示未找到。

由于是学习 node.js 的 demo，为了简单起见我只用了一个页面，GET 返回空表单，POST 执行加密或解密动作，并返回结果。前端用了 pure.css，一个很简单的 CSS 框架，只为了效果不要太挫。

在 mongodb 的使用上，我没有用官方的 mongodb driver，而是用了 mongoose。这是出于两点考虑：一是尽管 mongodb 很灵活，但在将来的网站建设中，绝不可能做到 schemeless，否则在设计类似用户系统这样的模块时会很痛苦；二是 mongoose 除了提供了一个 Schema，其他诸如 CRUD 的操作基本还是遵循原生 mongodb driver 的语法，因此并不影响对 mongodb 的理解。

在 web 框架的选择上，我决定先尝试 express.js。在此之前我曾搜过 "node.js web framework comparison"，其中有篇[文章](https://www.airpair.com/node.js/posts/nodejs-framework-comparison-express-koa-hapi)写的不错，较为详尽地分析了三个较为流行的框架 express、koa 以及 hapi。

express 是元老级的框架了，几乎和 node.js 是同时出现的，在 Github 上 有 16158 个 stars。它是个微框架（micro-framework），在 http 协议上封装了一层。npmjs 上已有成千上百的基于 express 的中间件，用于解决各类的问题。

koa 是个新型的框架，基于 ES6，Github 上有 4846 个 stars。其突出的特点是用了 ES6 的 generators 实现了协程，可以增加异步编程的可读性——这点和 Tornado 很相似。目前的版本是 0.13，尚未稳定，不敢贸然采用。

hapi 则是另一种风格，Github 上也有 3283 个 stars。其理念是 用配置代替代码，这在设计 REST API 时是十分方便的，在后续的学习中我可以适当地了解一下。

### 初始化

`nodejs`、`npm`、`mongodb` 这些必要程序的安装就不用说了。mongodb 和 MySQL 不同，不用做额外的配置，装完就可以用。

先建目录：

```sh
$ mkdir md5cracker && cd md5cracker
$ npm init
```

一路回车——虽然我知道这样不好，但这毕竟只是一个 demo。

装依赖：

```sh
$ npm install --save mongodb mongoose express es6-promise
```

这里`es6-promise`是`mongoose`的一个依赖，不知为何要单独拿出来安装。

辅助工具：

```sh
$ npm install -g nodemon express-generator
```

`nodemon`是一个方便的小程序，可以实时检测你的代码库，并在出现变更时重启服务器；`express-generator`，正如其名，用于生成 express 网站骨架。

这里要赞美一下 npm 3：在低版本的 npm 中，依赖的安装是树状结构的，不同的包不能共享依赖——这对有代码体积洁癖的人来说简直不能忍。npm 3 有许多新的特性，其一便是“依赖扁平化”——应该说，这才是正常的做法。

编辑`package.json`：

```js
{
  // ...
  "scripts": {
    "start": "nodemon ./bin/www"
  },
  // ...
}
```

这是为了简化网站的启动命令，完成后使用`npm start`即可启动网站，而不必每次都键入`nodemon ./bin/www`。

新建`nodemon.json`：

```js
{
    "execMap": {
        "js": "node --harmony"
    }
}
```

这是`nodemon`的配置文件，`node`的`--harmony`的参数能够启用 ES6 语法。

### mongodb

和 mysql 类似，mongodb 也需要初始化连接的代码。在 `app.js` 加入下列语句：

```js
// ...
var app = express();

// set up mongodb engine.
var mongoose = require('mongoose');
var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
mongoose.connect('mongodb://localhost:27017/crack');

// ...
```

事实上，这并不是最佳实践。毕竟，并不是所有的请求都会访问数据库，而且所有的请求都依赖于一个连接，可能会带来性能的损失。这里只是一个示范，暂时先不复杂化。

接下来便是 model 的定义：

（未完待续）