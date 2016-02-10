---
layout: post
title: Python “黑魔法” 之 Meta Classes
categories: 编程
tags:
 - python
 - Meta Classes
 - 黑魔法
 - 元编程
---

接触过 Django 的同学都应该十分熟悉它的 ORM 系统。对于 python 新手而言，这是一项几乎可以被称作“黑科技”的特性：只要你在`models.py`中随便定义一个`Model`的子类，Django 便可以：

 + 获取它的字段定义，并转换成表结构
 + 读取`Meta`内部类，并转化成相应的配置信息。对于特殊的`Model`（如`abstract`、`proxy`），还要进行相应的转换
 + 为没有定义`objects`的`Model`加上一个默认的`Manager`

开发之余，我也曾脑补过其背后的原理。曾经，我认为是这样的：

 > 启动时，遍历`models.py`中的所有属性，找到`Model`的子类，并对其进行上述的修改。

当初，我还以为自己触碰到了真理，并曾将其应用到实际生产中——为 SAE 的 KVDB 写了一个类 ORM 系统。然而在实现的过程中，我明显感受到了这种方法的丑陋，而且性能并不出色（因为要遍历所有的定义模块）。

那么事实上，Django 是怎么实现的呢？

> 自古以来我们制造东西的方法都是“自上而下”的，是用切削、分割、组合的方法来制造。然而，生命是自下而上地，自发地建造起来的，这个过程极为低廉。
> <cite>——王晋康 《水星播种》</cite>

这句话揭示了生命的神奇所在：**真正的生命都是由基本物质自发构成的，而非造物主流水线式的加工**。

那么，如果 类 也有生命的话，对它自己的修饰就不应该由调用者来完成，而应该是**自发的**。

幸而，python 提供了造物主的接口——这便是 Meta Classes，或者称为“元类”。

<!--more-->

## 元类 是什么？

简单说：元类就是**类的类**。

首先，要有一个概念：

### python 中，一切都是对象。

没错，一切，包括 类 本身。

既然，类 是 对象，对象 是 类的实例，那么——类 也应该有 类 才对。

### 类的类：type

在 python 中，我们可以用`type`检测一个对象的类，如：

```python
print type(1) # <type 'int'>
```

如果对一个类操作呢？

```python
print type(int) # <type 'type'>

class MyClass(object): pass

print type(MyClass) # <type 'type'>

print type(type) # <type 'type'>
```

这说明：`type`其实是一个类型，所有类——包括`type`自己——的类都是`type`。

### type 简介

从 [官方文档](https://docs.python.org/2/library/functions.html#type) 中，我们可以知道：

 + 和 `dict` 类似，`type` 也是一个工厂构造函数，调用其将返回 一个`type`类型的实例（即 类）。
 + `type` 有两个重载版本：
     + `type(object)`，即我们最常用的版本。
     + `type(name, bases, dict)`，一个更强大的版本。通过指定 类名称（`name`）、父类列表（`bases`）和 属性字典（`dict`） 动态合成一个类。

     下面两个语句等价：

     ```python
     class Integer(int):

        name = 'my integer'

        def increase(self, num):
            return num + 1

    # -------------------

    Integer = type('Integer', (int, ), {
        'name': 'my integer',
        'increase': lambda self, num: \
                        num + 1    # 很酷的写法，不是么
    })
    ```

也就是说：**类的定义过程，其实是`type`类型实例化的过程**。

**然而这和修饰一个已定义的类有什么关系呢？**

当然有啦～既然“类的定义”就是“`type`类型的初始化过程”，那其中必定会调用到`type`的构造函数(`__new__()` 或 `__init__()`)。只要我们继承 `type`类 并修改其 `__new__`函数，在这里面动手脚就可以啦。

接下来我们将通过一个栗子感受 python 的黑魔法，不过在此之前，我们要先了解一个语法糖。

### \_\_metaclass\_\_ 属性

有没觉得上面第二段示例有些鬼畜呢？它勒令程序员将类的成员写成一个字典，简直是反人类。如果我们真的是要通过修改 元类 来改变 类 的行为的话，似乎就必须采用这种方法了～～简直可怕～～

好在，[python 2.2](https://docs.python.org/2/reference/datamodel.html?#__metaclass__) 时引进了一个语法糖：`__metaclass__`。

```python
class Integer(int):

    __metaclass__ = IntMeta
```

现在将会等价于：

```python
Integer = IntMeta('Integer', (int, ), {})
```

由此一来，我们在使用传统类定义的同时，也可以使用元类啦。

## 栗子：子类净化器

> #### 需求描述
> 你是一个有语言洁癖的开发者，平时容不得别人讲一句脏话，在开发时也是如此。现在，你写出了一个非常棒的框架，并马上要将它公之于众了。不过，你的强迫症又犯了：如果你的使用者在代码中写满了脏话，怎么办？岂不是玷污了自己的纯洁？

假如你就是这个丧心病狂的开发者，你会怎么做？

在知道元类之前，你可能会无从下手。不过，这个问题你可以用 元类 轻松解决——只要在类定义时过滤掉不干净的字眼就好了（百度贴吧的干活～～）。

我们的元类看起来会是这样的：

```python

sensitive_words_list = ['asshole', 'fuck', 'shit']

def detect_sensitive_words(string):
    '''检测敏感词汇'''
    words_detected = filter(lambda word: word in string.lower(), sensitive_words_list)

    if words_detected:
        raise NameError('Sensitive words {0} detected in the string "{1}".' \
            .format(
                ', '.join(map(lambda s: '"%s"' % s, words_detected)),
                string
            )
        )

class CleanerMeta(type):

    def __new__(cls, class_name, bases, attrs):
        detect_sensitive_words(class_name) # 检查类名
        map(detect_sensitive_words, attrs.iterkeys()) # 检查属性名

        print "Well done! You are a polite coder!" # 如无异常，输出祝贺消息

        return super(CleanerMeta, cls).__new__(cls, class_name, bases, attrs)
        # 重要！这行一定不能漏！！这回调用内建的类构造器来构造类，否则定义好的类将会变成 None

```

现在，只需这样定义基类：

```python
class APIBase(object):

    __metaclass__ = CleanerMeta

    # ...
```

那么所有 `APIBase` 的派生类都会接受安全审查（奸笑～～）：

```python
class ImAGoodBoy(APIBase):

    a_polite_attribute = 1

# [Output] Well done! You are a polite coder!

class FuckMyBoss(APIBase):

    pass

# [Output] NameError: Sensitive words "fuck" detected in the string "FuckMyBoss".

class PretendToBePolite(APIBase):

    def __fuck_your_asshole(self):
        pass

# [Output] NameError: Sensitive words "asshole", "fuck" detected in the string "_PretendToBePolite__fuck_your_asshole".
```

看，即使像最后一个例子中的私有属性也难逃审查，因为它们本质都是相同的。

甚至，你还可以对有问题的属性进行偷偷的修改，比如 让不文明的函数在调用时打出一行警告 等等，这里就不多说了。

## 元类 在实际开发中的应用

日常开发时，元类 常用吗？

当然，Django 的 ORM 就是一个例子，大名鼎鼎的 SQLAlchemy 也用了这种黑魔法。

此外，在一些小型的库中，也有 元类 的身影。比如 `abc`（奇怪的名字～～）——这是 python 的一个内建库，用于模拟 抽象基类（Abstract Base Classes）。开发者可以使用 `abc.abstractmethod` 装饰器，将 指定了 `__metaclass__ = abc.ABCMeta` 的类的方法定义成 抽象方法，同时这个类也成了 抽象基类，抽象基类是不可实例化的。这便实现了对 抽象基类 的模拟。

倘若你也有需要动态修改类定义的需求，不妨也试试这种“黑魔法”。

## 小结

 + 类 也是 对象，所有的类都是`type`的实例
 + 元类（Meta Classes）是类的类
 + `__metaclass__ = Meta` 是 `Meta(name, bases, dict)` 的 语法糖
 + 可以通过重载元类的 `__new__` 方法，修改 类定义 的行为
