---
layout: post  
published: true   
title: 【HFMUN重构系列】4. Restful API 框架    
categories: HFMUN重构系列
---

## 0x01 什么是REST

“REST”这个词，也许会在许多场合上出现，但并不是每个人都理解它的意思。在维基百科中，它被定义为：

> **Representational State Transfer (REST)** is a software architecture style consisting of guidelines and best practices for creating scalable web services. REST is a coordinated set of constraints applied to the design of components in a distributed hypermedia system that can lead to a more performant and maintainable architecture.    —— From [Wikipedia](http://en.wikipedia.org/wiki/Representational_state_transfer)

也就是说：**REST，它不是一种技术，也不是一种标准，而是一种网络资源访问模式，一种编程哲学**。狭义上来说，REST指的是这样的设计思想：

 1. 每一个 URI 代表一种资源
 2. 客户端和服务器之间，传递这种资源的某种表现层
 3. 客户端通过五个 HTTP 动词（GET，POST，PUT，PATCH，DELETE），对服务器端资源进行操作，实现"表现层状态转化"（State Transfer）

狭义的 REST 范式是基于 B/S 架构，并使用 HTTP 协议进行数据交互。比起古老而笨重的 SOAP 等架构，这种模式更加轻便、直观，使网络资源的访问变得简洁、优雅，也更加符合当今 Web 开发的需求。

## 0x02 如何正确使用 REST

正如上面所说，REST 是基于 HTTP 协议的。它用 URI 来定义资源，并用 HTTP 请求来操作资源。然而，并不是说使用了 HTTP 协议即可称之为 REST——真正意义上的 REST，有自己的一套准则。也正是这套准则，才使得 REST 简洁、优雅。

### REST 是语义的

语义的（Semantic）是指：**资源的 URI 或是资源的访问必须是有意义的，符合或尽量符合自然语言的规范**。

举个例子：如果我要访问订单的列表，那么一个良好的 URI 定义应该是这样的：

```http
GET /orders/ HTTP/1.1
```

资源的 URI 通常由名词组成，这也正符合自然语言的规范——表达一个物体，人们使用名词。

如果要精确定位某一个资源，通常需要进一步限制资源：

```http
GET /orders/1/ HTTP/1.1
```

或是：

```http
GET /orders/current/ HTTP/1.1
```

甚至，可以表示资源的从属关系：

```http
GET /users/current/orders/1/ HTTP/1.1
```

这就像在和服务器对话一样：**“请给我当前用户的第一份订单”**。

而一些与资源本身无关的信息，比如列表的最大数目，可以放到 URI Params 中：

```HTTP
GET /orders/?limit=20 HTTP/1.1
```

HTTP协议中的动词（Verbs），通常用来描述对资源的操作。每一种动词都有它自己的意义：

 * **GET**——获取资源
 * **POST**——建立一个新的资源
 * **PUT**——修改一个资源，必须提交该资源的所有内容
 * **PATCH**——修改一个资源，可以只提交该资源的一部分内容
 * **DELETE**——删除一个资源
 
### REST 是多样的 
 
至于返回的数据，服务器端可以提供多种格式供客户端选择，如 JSON、XML、YAML等等，通常用格式的缩写作为尾缀：

```http
GET /orders.json/ HTTP/1.1
```

### REST 是健壮的

倘若用户请求的资源不存在或是提交的数据不合规范，服务器必须以**HTTP状态码**的方式通知客户端。常用的状态码有：

 + **400** 请求参数有误
 + **401** 用户未登录
 + **403** 没有权限
 + **404** 资源找不到

## 0x03 django 中的 REST

像 REST 这么高大上的东西，早就有人对它进行了实现，这便是：[Django Rest Framework](http://www.django-rest-framework.org/)。基本的用法可以参见官网。

成熟的框架并不是最好的，只有适合自己的才是。在使用过程中我遇到了一系列的问题，并以自己的方式解决了他们。

### ViewSet 的路由不够 D.R.Y.

`ViewSet` 是 `rest_framework`中一个十分有创意的地方。它将 CRUD 操作集中到了一个类中，提高了代码的复用性。然而，每一个 `ViewSet` 都需要 定义一个 `Router` 进行 URL 路由，这很麻烦。于是乎我便想：

> 要是能让它自动感知`ViewSet`的存在并自动为其定义路由，就像`django`中的`Models`一样，那该多好啊

于是，我仿照`django.apps.registry`，写了一个能在启东时探知一个 app 中固定内容的 `app_cache` 模块：

```python
# app_cache/core.py

from django.utils.importlib import import_module
from django.utils.module_loading import module_has_submodule
from django.apps import apps

class AppCache(object):
    '''
    Inherit this class and override the fields below, then import and instantiate
    the subclass at AppConfig.ready method.
    '''

    module_name = ''
    object_name = ''
    default_object = ''

    def __init__(self, *args, **kwargs):
        self.__module_name = '.%s' % self.module_name

    def get_objects(self):
        for mod in self.get_modules():
            yield getattr(mod, self.object_name, self.default_object)

    def get_modules(self):

        for app_config in apps.get_app_configs():
            if not module_has_submodule(app_config.module, self.module_name):
                continue

            yield import_module(self.__module_name, app_config.name)
```

同时新建一个叫`api`的 app，在`api/core.py`中实现自动寻找`ViewSet`：

```python
from app_cache import AppCache

class APICache(AppCache):

    default_object = ()
    object_name = 'routers'
    module_name = 'routers'

    def get_routers(self):
        results = []
        for obj in self.get_objects():
            results.extend(obj)
        return results

cache = APICache()
```

在`api/urls.py`中实现自动路由：

```python
# api/urls.py

from django.conf.urls import url, patterns, include

from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSetMixin
from rest_framework.views import APIView

from .core import cache

extra_list = []
router = DefaultRouter()
for pattern, obj in cache.get_routers():
    if callable(obj) and not isinstance(obj, type) or isinstance(obj, basestring):
        extra_list.append(url(pattern, obj))
    elif issubclass(obj, ViewSetMixin):
        router.register(pattern, obj)
    elif issubclass(obj, APIView):
        extra_list.append(url(pattern, obj.as_view()))
                
extra_list.append(url(r'^', include(router.urls)))

urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'^root/$', 'api.views.root',),
    *extra_list
)
```

之后，只需在每个 app 中定义一个`routers.py`，并定义`routers`变量即可实现 `ViewSet` 的自动路由，例如：

```python
from .views import UserAPIViewSet

routers = (
    (r'users', UserAPIViewSet),
)
```

非常方便。

### 翻页机制的进一步改进

> #未完待续。。。