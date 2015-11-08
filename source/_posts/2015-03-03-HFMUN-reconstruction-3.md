---
layout: post
title: 【HFMUN重构系列】3. 消息系统
date: 2015-03-03 21:53:20.000000000 +08:00
categories:
- 编程
tags:
- HFMUN重构系列
---
> 一个真正优秀的系统，值得你无数次地去重构。

消息系统算是网站比较重要的一部分，它承担着将**已发生的事件通知给相关用户**的责任。看似简单，但若想做到DRY，实现起来却很复杂——因为，通知的类型太多了。

这个系统，在三个项目中我实现了三次。三次都使用不同的方法，但三次都不怎么满意。这最后一次，算是比较成功的一次了。

在第一版模联网站中，我采用了一个堪称最糟糕的方案（如图所示）：

![UML](/assets/wboard_notifications.jpg)

这个方案最大的缺点：

1.  **耦合度太高**。如果有一天，又多了一种消息类型，那么就要多加一张表。
2.  **查询的难度大**。通常来说我们需要显示所有的消息，从而需要使用JOIN语句进行多表联查——这效率是很低的。
3.  **SQL本身就不是面向对象的**。虽说`CommentNotification`是`Notification`的子类，可查询时却并不能使用类似`Notification.objects.all()`一类的语句。在一定程度上可以说：SQL本身就不是面向对象的。

而在第二版模联网站中，我采用了[泛型](https://docs.djangoproject.com/en/1.7/ref/contrib/contenttypes/)（Generic Model Relations）这一技术来实现——这是Django另一大特色：**通过记录对象的类型信息以及唯一标识符，实现了一种可以指向任何表的外键（GenericRelation）**。这种技术存在的目的就是为了**解耦合**，使系统扩展更具灵活性——尽管要损失一些效率，但与架构的“健康”比起来那是微不足道的，无可厚非。

UML图如下：

![UML](/assets/hfmun_notices.jpg)

这其中，`notice_type`的取值决定了**`url`域的作用**：

*   **`link`**。该消息的`url`域表示一个指向`related_object`的地址，应该展示给用户看。
*   **`invoke`**。该消息需要在用户确认后执行一个动作。其`url`域表示需要执行的动作的地址——这里有些TaskQueue的意味。

然而，发消息时又应该怎么做呢？如果在所有的地方都来一句：`Notice.create(......)`，那也太不DRY了吧？

有人说：“懒惰是程序员的天性。”

我赞同，但我还想补充一句：“懒惰更是程序员精简代码的动力。”

于是，我创立了一个类`NoticeDispatcher`，用于分发消息——其实这一类工具代码在之前的系统中也存在过，只不过这一版本的令我更为满意。

    class NoticeDispatcher(object):

        def __init__(self, model, default = {}):
            if not issubclass(model, SendNoticeModelMixin):
                raise TypeError('The `model` must be a subclass of  `SendNoticeModelMixin`.')
            self.__model = model
            self.__default = {}
            self.__default.update(default)

        def send(self, *args, **kwargs):
            klass = Notice

            title = self.__model.generate_title(*args, **kwargs) 
            content = self.__model.generate_content(*args, **kwargs) 
            url = self.__model.generate_url(*args, **kwargs)
            user = self.__model.generate_user(*args, **kwargs)

            valid_keys_set = set(kwargs.iterkeys()) & \
                set(field.name for field in klass._meta.fields)

            params = deepcopy(self.__default)
            params.update({key: kwargs[key] for key in valid_keys_set})
            params.update({
                'title': title,
                'content': content,
                'url': url,
            })

            results = []
            try:
                iter(user)
            except:
                user = (user,)

            for _user in user:
                params['user'] = _user
                notice = klass(*args, **params)
                notice.save()
                results.append(notice)

            return results

我们可以传入一个模型类作为参数从而获得一个`NoticeDispatcher`对象。这个模型类被要求继承于`notices.mixins.SendNoticeModelMixin`，以完成一些默认的配置——这是一个抽象基类：

    class SendNoticeModelMixin(object):

        @classmethod
        def generate_title(klass, *args, **kwargs):
            return ''

        @classmethod
        def generate_content(klass, *args, **kwargs):
            return ''

        @classmethod
        def generate_url(klass, *args, **kwargs):
            return ''

        @classmethod
        def generate_user(klass, *args, **kwargs):
            return []

做完这一切之后，每当调用`notice_dispatcher.send()`方法时，`NoticeDispatcher`会自动调用模型类中的`generate_*`方法以获取构建消息对象的默认参数。像一些基本不变的内容——如`url`、`title`就可以用代码自动生成，进而提高代码复用率。

当然，这个系统仍有一些不够完善的地方，如：

*   `notice_type`为`invoke`时的逻辑至今尚未实现。
*   当消息的构建不需要`related_object`参数时，仍需调用原生的`create`方法，非常麻烦。
*   `related_object`参数仍需手动传入，有些不干净——最好就是能在`SendNoticeModelMixin`上实现`send`方法，很多啰嗦的代码便又可以省略掉了。

以上问题，或是由于没有需求，或是由于懒惰（- -!），没有来得及去实现。但愿能在下一次改进时解决。

总而言之呢，事情正在似乎在朝着好的方面发展。