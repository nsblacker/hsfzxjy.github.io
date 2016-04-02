---
layout: post
title: 17 行代码实现的简易 Javascript 字符串模板
categories: 编程
tags:
 - javascript
 - DIY
 - 字符串模板
 - 正则表达式
---

这是源于两年前，当我在做人生中第一个真正意义上的网站时遇到的一个问题

该网站采用前后端分离的方式，由后端的 REST 接口返回 JSON 数据，再由前端渲染到页面上。

同许多初学 Javascript 的菜鸟一样，起初，我也是采用拼接字符串的形式，将 JSON 数据嵌入 HTML 中。开始时代码量较少，暂时还可以接受。但当页面结构复杂起来后，其弱点开始变得无法忍受起来：

 + **书写不连贯**。每写一个变量就要断一下，插入一个 `+` 和 `"`。十分容易出错。
 + **无法重用**。HTML 片段都是离散化的数据，难以对其中重复的部分进行提取。
 + **无法很好地利用 `<template>` 标签**。这是 HTML5 中新增的一个标签，标准极力推荐将 HTML 模板放入 `<template>` 标签中，使代码更简洁。

当时我的心情就是这样的：

![](http://i6.hexunimg.cn/2012-05-09/141219425.jpg)

为了解决这个问题，我暂时放下了手上的项目，花了半个小时实现一个极简易的字符串模板。

<!--more-->

## 需求描述

实现一个 `render(template, context)` 方法，将 `template` 中的占位符用 `context` 填充。要求：

 1. 不需要有控制流成分（如 循环、条件 等等），只要有变量替换功能即可
 2. 级联的变量也可以展开
 3. 被转义的的分隔符 `{` 和 `}` 不应该被渲染，分隔符与变量之间允许有空白字符

例子：

```javascript
render('My name is {name}'， {
    name: 'hsfzxjy'
});  // My name is hsfzxjy

render('I am in {profile.location}', {
    name: 'hsfzxjy',
    profile: {
        location: 'Guangzhou'
    }
}); // I am in Guangzhou

render('{ greeting }. \\{ This block will not be rendered }', {
    greeting: 'Hi'
}); // Hi. { This block will not be rendered }
```

## 实现

先写下函数的框架：

```javascript
function render(template, context) {

}
```

显然，要做的第一件事便是 **匹配模板中的占位符**。

### 匹配占位符

匹配的事，肯定是交给正则表达式来完成。那么，这个正则表达式应该长什么样呢？

根据 需求 1、2 的描述，我们可以写出：

```javascript
var reg = /\{([^\{\}]+)\}/g;
```

至于需求 3，我第一个想到的概念是 **前向匹配**，可惜 Javascript 并不支持，只好用一个折衷的办法：

```javascript
var reg = /(\\)?\{([^\{\}\\]+)(\\)?\}/g;
// 若是第一个或第三个分组值不为空，则不渲染
```

现在，代码应该是这样：

```javascript
function render(template, context) {

    var tokenReg = /(\\)?\{([^\{\}\\]+)(\\)?\}/g;

    return template.replace(tokenReg, function (word, slash1, token, slash2) {
        if (slash1 || slash2) {  // 匹配到转义字符
            return word.replace('\\', ''); // 如果 分隔符被转义，则不渲染
        }

        // ...
    })
}
```

### 占位符替换

嗯，正则表达式确定了，接下来要做的便是替换工作。

根据 需求2，模板引擎不仅要能渲染一级变量，更要渲染多级变量。这该怎么做呢？

其实很简单：将 `token` 按 `.` 分隔开，逐级查找即可：

```javascript
var variables = token.replace(/\s/g, '').split('.'); // 切割 token
var currentObject = context;
var i, length, variable;

// 逐级查找 context
for (i = 0, length = variables.length; i < length; ++i) {
    variable = variables[i];
    currentObject = currentObject[variable];
}

return currentObject;
```

不过，有可能 `token` 指定的变量并不存在，这时上面的代码便会报错。为了更好的体验，代码最好有一定的容错能力：

```javascript
var variables = token.replace(/\s/g, '').split('.'); // 切割 token
var currentObject = context;
var i, length, variable;

for (i = 0, length = variables.length; i < length; ++i) {
    variable = variables[i];
    currentObject = currentObject[variable];
    if (currentObject === undefined || currentObject === null) return ''; // 如果当前索引的对象不存在，则直接返回空字符串。
}

return currentObject;
```

把所有的代码组合在一起，便得到了最终的版本：

```javascript
function render(template, context) {

    var tokenReg = /(\\)?\{([^\{\}\\]+)(\\)?\}/g;

    return template.replace(tokenReg, function (word, slash1, token, slash2) {
        if (slash1 || slash2) {  
            return word.replace('\\', '');
        }

        var variables = token.replace(/\s/g, '').split('.');
        var currentObject = context;
        var i, length, variable;

        for (i = 0, length = variables.length; i < length; ++i) {
            variable = variables[i];
            currentObject = currentObject[variable];
            if (currentObject === undefined || currentObject === null) return '';
        }

        return currentObject;
    })
}
```

除去空白行，一共 17 行。

## 将函数挂到 String 的原型链

甚至，我们可以通过修改原型链，实现一些很酷的效果：

```javascript
String.prototype.render = function (context) {
    return render(this, context);
};
```

之后，我们便可以这样调用啦：

```javascript
"{greeting}! My name is { author.name }.".render({
    greeting: "Hi",
    author: {
        name: "hsfzxjy"
    }
});
// Hi! My name is hsfzxjy.
```
