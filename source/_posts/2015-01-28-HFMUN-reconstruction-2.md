---
layout: post
title: 【HFMUN重构系列】2. 用户系统
date: 2015-01-28 20:41:10.000000000 +08:00
categories:
- 编程
tags:
- HFMUN重构系列
---
> 现在，我比任何时候都要有主见。

这是这次重构过程中我最想说的一句话了。

毋庸置疑，Django是一个十分优秀的Web框架：高效的开发模式，完备的应用集成，以及最重要的一点——具有完全自由的扩展能力——这是Django的灵魂所在。但是无知，通常会束缚了一个人的探索欲望与创新能力，让其变得胆怯、变得懒惰。一年前我的遭遇就很好地印证了这一点。

对于一个网站而言，用户永远是最重要的元素。没有了用户，网站做得再好也只能被放在角落腐烂，与死尸无异。这样看来，打造一个完美的用户系统就显得十分必要了。

Django为我们提供了一个优秀的用户系统，它位于`django.contrib.auth`——想必Djangoers都对它很熟悉了。`auth`应用是专门为用户管理打造的一个应用，它提供了以下功能：

*   一个用户模型（User）。这是`auth`框架的核心所在，用于存储用户信息，包括 用户名、密码、邮箱等内容。该模型可被替换也可被拓展，具有良好的可塑性。
*   一个权限系统（Permission）。这部分为实现访问控制提供了可能。一个`Permission`对应一个关于`Model`的操作，默认有`add`、`change`、`delete`三种。值得一提的是，在版本`1.7`之前，Django并不提供更改默认权限的能力，即每个`Model`都会固定拥有以上三种权限。我个人觉得这种做法不太好，并不是所有的模型都需要这种功能划分。更何况权限限制被应用在Django的每一个角落，如果想让一个模型完全开放，就要多敲许多不必要的代码。如今Django1.7改进了这一点，这使得模型更加简洁了。
*   用户分组的功能（Groups）。一个`Group`可以拥有多个`Permission`，一个用户可以选择加入一个`Group`，并会自动拥有还`Group`的权限。这一设计简化了用户管理的操作，同时也让用户系统的更有层次。

在这里，我想说的是关于扩展`User`模型的一些技巧。

一年之前，由于对Django的不了解，我不敢对它的内部实现大动干戈。而事实上，没有什么东西是绝对完美的，即便是集众智于一身的开源框架也是如此。诚然，`auth`框架是不错，但在某些特定的应用场景，它便显得心有余而力不足了。因此，我希望能在`User`模型上附带一些额外的信息。

百度一下，我找到了一个被广为流传的方法：`Profile`模式。也就是说，额外定义一个`Profile`模型和`User`模型建立一一对应的关系，用于储存额外信息。我清楚地记得，几乎是每一篇博客都在介绍这种方法，于是乎我毫不犹豫地就采纳了。现在想一想，这其实是一个十分糟糕的方案。它有如下缺点：

*   **操作麻烦。**每次访问额外信息，都要先询问是否存在`Profile`对象，如果不存在得先创建。然后再调用`user_object.profile`来访问信息。同时，这种方案对表单不友好，因为用户信息是被分开储存在两个表中的。
*   **效率低下。**每次访问额外信息，先是用`IF EXISTS`判断是否存在，再用`INNER JOIN`将主信息和次信息从数据库中取出，一共需要两条SQL语句。更何况，`INNER JOIN`指令是公认的效率低下的指令。

因此，在这次重构中我采用了一种截然不同的做法：直接重写`User`模型。这里的灵感来自[Django官方文档](https://docs.djangoproject.com/en/1.7/topics/auth/customizing/#auth-custom-user)：

> Some kinds of projects may have authentication requirements for which Django’s built-in User model is not always appropriate. For instance, on some sites it makes more sense to use an email address as your identification token instead of a username.
> 
> Django allows you to override the default User model by providing a value for the AUTH_USER_MODEL setting that references a custom model:
> 
>      AUTH_USER_MODEL = 'myapp.MyUser'

听起来不错，既方便实现起来又简单。于是我重写了我的`accounts`应用：

    #encoding=utf8
    """
        事实上这里许多实现都模仿自`django.contrib.auth.models.User`，毕竟我只是要存储一些额外信息而已。
    """
    from django.core import validators
    from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
    from django.utils.translation import ugettext_lazy as _
    from django.utils import timezone
    from django.db import models

    class UserManager(BaseUserManager):

        def _create_user(self, username, password,
                         is_staff, is_superuser, **extra_fields):
            """
            Creates and saves a User with the given username, email and password.
            """
            now = timezone.now()
            if not username:
                raise ValueError('The given username must be set')
            user = self.model(username=username,
                              is_staff=is_staff, is_active=True,
                              is_superuser=is_superuser, last_login=now,
                              date_joined=now, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_user(self, username, password=None, **extra_fields):
            return self._create_user(username, password, False, False,
                                     **extra_fields)

        def create_superuser(self, username, password, **extra_fields):
            return self._create_user(username, password, True, True,
                                     **extra_fields)

    # 这里的`AbstractBaseUser`是用户模型的基类，由于原生的`User`模型中有一些字段并不是我想要的，因此我需要从上一个抽象类继承。
    class User(AbstractBaseUser, PermissionsMixin):

        username = models.CharField(_('username'), max_length=30, unique=True,
            help_text=_('Required. 30 characters or fewer. Letters, digits and '
                        '@/./+/-/_ only.'),
            validators=[
                validators.RegexValidator(r'^[\w.@+-]+$', _('Enter a valid username.'), 'invalid')
            ])

        # 用户描述
        description = models.TextField()

        # 昵称
        nickname = models.CharField(_('nickname'),
            max_length=30, unique=True,
            help_text=_('Required. 30 characters or fewer.'),
            )

        # 好友关系
        friends = models.ManyToManyField(
            'self',
            verbose_name=_('friends'),
            blank=True,
            related_name='+'
            )

        #================以下是原有的字段==================
        is_staff = models.BooleanField(_('staff status'), default=False,
            help_text=_('Designates whether the user can log into this admin '
                        'site.'))
        is_active = models.BooleanField(_('active'), default=True,
            help_text=_('Designates whether this user should be treated as '
                        'active. Unselect this instead of deleteing accounts.'))
        date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

        USERNAME_FIELD = 'username'
        objects = UserManager()

        class Meta:
            verbose_name = _('user')
            verbose_name_plural = _('users')

        def get_full_name(self):
            return self.nickname

        def get_short_name(self):
            return self.nickname

以及`settings.py`文件：

    #...
    AUTH_USER_MODEL = 'accounts.User'
    #...

为了让admin框架同步支持我们的新`User`模型，还需要对`admin.py`以及`forms.py`进行相应的修改，实际上就是把新加入的字段写进相应的类即可，在这里我就不贴代码了。

做完这一切，一个念头忽然从我脑海中闪过：对于一些第三方应用，如果它们直接引用了`django.contrib.auth.models.User`，那该怎么办呢？我的`User`模型会生效吗？

这让我感到不安，因为重构的一大原则便是：不得改变外部接口的调用情况。如果这一改动使得整个网站都崩溃了，那就得不偿失了。可庆幸的是，这样的事情并没有发生。

这不禁让我感到好奇：django是怎么做到这一点的？

翻看`django.contrib.auth.models`，我发现了如下一句代码：

    class User(AbstractUser):
        """
        Users within the Django authentication system are represented by this
        model.

        Username, password and email are required. Other fields are optional.
        """
        class Meta(AbstractUser.Meta):
            swappable = 'AUTH_USER_MODEL'

查找[Django文档](https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey.swappable)，原来这是Django1.7的一个新特性：

> **ForeignKey.swappable**
> 
> Controls the migration framework’s reaction if this ForeignKey is pointing at a swappable model. If it is True - the default - then if the ForeignKey is pointing at a model which matches the current value of settings.AUTH_USER_MODEL (or another swappable model setting) the relationship will be stored in the migration using a reference to the setting, not to the model directly.
> 
> You only want to override this to be False if you are sure your model should always point towards the swapped-in model - for example, if it is a profile model designed specifically for your custom user model.
> 
> Setting it to False does not mean you can reference a swappable model even if it is swapped out - False just means that the migrations made with this ForeignKey will always reference the exact model you specify (so it will fail hard if the user tries to run with a User model you don’t support, for example).
> 
> If in doubt, leave it to its default of True.

这个特性可以使指向这个模型的ForeignKey自动被替换成`Meta.swappable`的内容，实现模型的可替换能力。这是一个巧妙的设计。

重构后的`accounts`应用，逻辑变得更加清晰，也使我不再纠结于冗长的恼人的`Profile`调用。

这，是一个美妙的起点。