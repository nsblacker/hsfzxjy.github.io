---
layout: post
published: true
title: 【译】响应式图片的现状
categories: 翻译 编程 web设计
---

> 原文链接：[戳这里](http://www.webdesignerdepot.com/2015/08/the-state-of-responsive-images/)

![](http://netdna.webdesignerdepot.com/uploads/2015/08/featured_images1.jpg)

Web 是一种可视化的媒体。绚丽的视觉效果，很大程度上离不开图片文件所作出的贡献。虽然（Whilst）其中的许多效果都可以用 CSS 和 内联 SVG 来实现，互联网上的许多站点仍需要图片文件。

从去年的统计来看，每个站点中，图片平均占了一半的页面体积，并且随着时间的推移，图片体积有持续增加的趋势；就 2014 年而言，图片的大小便增长了 **21%**。

与此同时，互联网终端的种类、数量也在增长。从 72 ppi（市场份额正在下降）到 600 ppi，不同设备的分辨率（resolution）有着天壤之别。

创建能在任何设备中都有着高质量的图片，其实再容易不过了——用 1000 ppi 的质量保存图片，然后就可以不用再理他了（译者注：原文是 call it a day）。生成的图片，即使是在分辨率最高的设备上查看也是十分清晰的（crisp）。但是，在图片质量提升的同时，图片文件的大小也会相应地增加。要知道，**页面加载时间**可是影响用户体验的**首要因素**——因此，保证站点能够及时地呈现在用户面前是我们义不容辞（incrumbent）的责任。高质量的图片，即使是在宽带环境下加载也要耗费几十秒，更不用说（let alone）是移动端的设备了——简直就是无法使用。

响应式图片的目的，不是要为设备提供尽可能高质量的图片（这一点，我们很容易做到），而是要为设备提供它所能支持的最高质量的图片，仅此而已（nothing more）。

从这篇指南中，你将了解到响应式图片的工作原理（what works），响应式图片仍然存在的问题和陷阱（pitfall），以及如何将响应式图片运用到网站中。

<!--more-->

## 我能感受到这欲望，对速度的渴求

为什么速度这么重要？难道还有人在用 3G 网络吗（译者注：歪果仁科技发达，早已看不起 3G 网络）？如果你的目标客户都住在曼哈顿市中心，为什么还要为莱索托的乡巴佬担心呢（译者注：南非山区）？ 事实上，“每个人都能用上超快的宽带，用上由那些利欲熏心的公司提供的宽带”——听起来就像个神话。

每个人每天都要耗费至少两个小时在恶劣的（inferior）网络环境中。就我而言，在挤公交上下班时（commuting），我常常会上网以打发无聊的时光——每当这时，稳定的 3G 网络听起来都像是遥不可及的美梦。

今年四月的时候，[Google 声称](http://googlewebmastercentral.blogspot.co.uk/2015/04/rolling-out-mobile-friendly-update.html)“‘移动设备友好性’将会成为移动站点的排名因素“。甚至，在此之前，[加载速度也是一个重要的排名因素](http://googlewebmastercentral.blogspot.co.uk/2011/03/introducing-page-speed-online-with.html)——无论是显式地体现在 Google 的统计中，抑或是隐式地成为影响网站跳出率（bounce rate）的一个重要因素。

对于两个相近的站点，1Kb 的冗余数据，都可能将你的 Google 排名从第三降到第四、第五，甚至是第十、第十一——换言之，从第一页降到了第二页——这会给你的收入（revenue）带来不小的冲击。

## 你真的需要这图片吗？

图片优化的最高境界便是：没有图片。你的站点上有五张图片，去掉一张，你便节省了 20%——或许更重要地，你节省了一次 HTTP 请求。如果你将五张图片都去掉了，那你就节省了 100%，以及所有的 HTTP 请求。因此，何乐而不为呢？

然而，我们并不会这么做——毕竟在短期内，图片比文字更有感染力。它们能和用户建立一种”感情通道“，从而使用户被站点的内容所吸引。

要知道，[用户从来不读网页](http://www.nngroup.com/articles/how-little-do-users-read/)——只有极少数人会深入阅读站点上的内容。图片能让我们在很短的时间（a fraction of time）内了解一个品牌，深深地记住它（reinforce）——这是文字做不到的。

也许，图片的体积会很大，加载起来显得很笨重。然而一旦被浏览器渲染出来，和文字相比，它们能够更有力地抓住用户的眼球，更高效地传达品牌信息。

而响应式图片，就是为了更好地把握住这来之不易的”感情通道“，以防不耐烦的用户点击点击了”后退“按钮。

## 那么，SVG 又怎么样呢？

SVG（可缩放矢量图像）是 Web 发展史上的一大创举。它引领着潮流（ahead of the curve），至今大多数设计师依旧没有意识到其真正的潜力。

SVG ——正如它的名字所描述——是基于矢量的。这意味着 SVG 图像是由点、角和直线构成的。SVG 同时也是——正如它的名字所描述——是可缩放的，这意味着在 5k iMac 和 Android 智能手机上，它会表现得同样出色——没有质量的损失，也没有体积的差别。

如果你需要一张平面插图（flat illustration），一个图标，一个 logo 以及其他所有能够以 SVG 的形式显示出来的东西，SVG 是不二之选（the way to go）。

Web 上大多数图片都是位图。一般来说，位图的工作原理就是将每个像素点依次描述出来，包括它们的颜色（RGB 的形式，即 红、绿、蓝值），以及透明度（在某些场景下）。如果你有一张尺寸为 100px × 100px 的图片，那么它将有 10000 个像素点。如果每个像素点都用 4 个值来描述，那么这张图将等同于 40000 bits 的数据。听起来很多，不是吗？然而有时，它们的体积会比矢量图还要小。

考虑 1px × 1px 的图片，若使用位图，则需要 4 bits 来记录（红、绿、蓝，以及透明度）。现在考虑用矢量的形式来记录相同尺寸的图片：除了 RGBA 颜色值之外，还需要矩形的左上角坐标、长度和宽度这几个量。

这都是些极端的（crude）情况，但它们是准确的。通常，如果一幅图片的矢量版本——假使有的话——比同样的（equivalent）位图占用的体积还要多，那么位图是唯一合理的选择。

## （错误地）使用 Javascript

正如生活中的许多问题（如果你的生活是在网络上的话），响应式图片也可以用 Javascript 来解决。事实上，在过去的许多年中，Javascript 是解决这个问题的唯一途径。通过对 User Agent 进行测试，Javascript 可以知道当前的浏览器类型，然后将指向合适的图片地址的 `image` 标签输出到页面上。

有些 Web 设计师反对这么做，理由是：[有些人会关闭 Javascript 功能](https://gds.blog.gov.uk/2013/10/21/how-many-people-are-missing-out-on-javascript-enhancement/)。然而，这种情况已经非常少见了，尤其是在移动设备中。尽管如此，这种方法仍存在着一些问题——比如，这种图片不会被搜索引擎机器人解析出来，而且只有当脚本执行后图片才会被加载出来。

事实上，使用 Javascript 最大问题是：这是一种有悖于 Javascript 主要目的的使用方式。HTML 管理数据，CSS 处理表现形式，而 Javascript 负责功能实现。当我们违背了这些既定规则时，我们就会遇到各种各样的问题，遇到需要”奇技淫巧“（hack）来解决的问题。图片的本质是数据，因此应该交由 HTML 来处理。

## 浏览器的问题

从 RWD （响应式网页设计，Responsive Web Design）提出至今，图片都是最大的绊脚石（stumbling block）。然而现在，我们要开始寻找方法来解决这各种各样的问题了。能够被称为”最佳实践“的，都是那些久经沙场的（battle-hardened）、有足够成功案例的技术。专业的（dedicated）开发者已经牺牲了自己的时间去去游说（lobby） W3C，以求获得官方的解决方案。而现在，响应式图片第一次成为了可能。

响应式图片的关键，在于它充分地意识到了 Web 的失败之处。为保证响应式图片不会使浏览器崩溃，设计者们早已考虑得十分周到——即使对于不支持响应式图片的浏览器，代码也不会报错，而是向用户展示一张默认的、非响应式的图片。

在这篇文章中，我们将见到两个官方的响应式图片标签：`srcset` 以及 `picture`。

截至目前，Edge、Safari 和 iOS Safari 只支持 `srcset` 的一部分特性。Firefox、Chrome、Opera、Android 内置浏览器以及下一个版本的 Safari 和 iOS Safari 都将会完整地支持它。（我们会在下文讨论它们的区别）

而 `picture` 元素，已经被 Firefox、Chrome、Opera 以及 Android 内置浏览器完美支持。Edge、Safari 和 iOS Safari 则完全不支持，并且暂时也没有实现它们的打算。

由于不同厂商解析 W3C 特性的方法不同，即使是在兼容它们的浏览器中，也有一些不一致的地方。例如，当你使用 viewport 的大小来区分不同的设备时，有些浏览器会在 viewport 比小图片大 1px 时便将小图切换为大图，而另外一些则在 viewport 完全符合大图显示条件时才会这么做。

总之，浏览器可以分为两大阵营：想要图片质量尽可能高的 以及 想要图片体积尽可能小的。浏览器厂商都在各自推崇（duking）自己的主张，直到某一方的实现被大众所认可——个人而言我喜欢后者，因为它认为性能对用户体验而言更加关键。

至于现在，Web 设计人员的最佳选择就是：坚持 W3C 标准，而不要对浏览器作额外的猜测。毕竟，浏览器的默认体验（高质量 或是 高性能）是由用户选择的默认浏览器决定的——因此，如果用户意识到这其中的区别，那么用户的偏好就最有可能成为浏览器的偏好（译者注：这里怪怪的）。

## 响应式图片最佳实践（2015）

纵观 Web 的历史，我们曾经用一个标签来表示图片：`img` 标签。在 HTML5 中，`img` 的角色经历了（undergone）一些微妙（subtle）的变化——它被设计成响应式图片的开关，即其不再代表一张图片，而只是响应式图片的占位符。

这其中的区别十分重要。曾经，`img` 标签只能持有一副图片的数据（位图 或 矢量图）——而现在，它能持有多幅图的数据。

`img`标签看起来是这样的（概括（recap）给非开发者）：

```html
<img src="" alt="" />
```

`img` 标签的响应式版本看起来是这样的：

```html
<img srcset="" src="" alt="" />
```

仅仅（Barely）只有一些区别而已。仔细看代码，你会注意到一件重要的事情：**代码是向后兼容的**。如果一个浏览器不能理解 `srcset` 属性，它会简单地忽略它，并按照 1993 年的原始标准进行渲染。

这意味着：我们能通过标记来使用响应式图片，而不需要对相关特性进行检测。

在新的响应式 `img` 标签中， 原则上 `src` 属性只是为不支持 `srcset` 的浏览器指定了默认的图片地址，而 `srcset` 属性则包含了用于适配各种分辨率的图片信息。

在渲染 `img` 标签是时，浏览器会自己决定出最适合的图片文件。

### 使用 srcset

既然我们已经知道 `srcset` 在不兼容的浏览器中会静默失败，我们便可以子有底增加图片了：

```html
<img srcset="image-b.jpg" src="image-a.jpg" alt="an image" />
```

在这个例子中，任何支持 `srcset` 的浏览器将会显示 `image-b.jpg`，而任何不支持的浏览器则会显示 `image-a.jpg`。

重要的是，你要知道浏览器只会下载它想要显示的图片，而并不会将所有图片都加载出来后再进行选择。

遗憾的是，我们并没有任何进步——除非我们是在展示 `srcset` 属性的使用，仅靠 `srcset` 的支持与否来加载图片并没有什么实际的应用。

解决方法就是：为浏览器提供更多的信息，让其知道自己该选择那一张图片。为了做到这一点，我们需要提供和图片的 像素密度（pixel density） 以及 可用空间（available space） 相关的信息。

### 使用 x 描述符

x 描述符能够让浏览器知道图片的像素密度。

举个例子，如果你想要提供一张两倍像素于标准图片的 视网膜级的（retina-grade）的图片，你需要在 `srcset` 中做出说明：在文件名后加上 `2x`。

这是我们的图片：

```html
<img src="image.jpg" alt="an image" />
```

为了给浏览器增添一个视网膜选项，我们将作出如下修改：

```html
<img srcset="retina-image.jpg 2x" src="image.jpg" alt="an image" />
```

在这个案例中，有三个可能的结果：


 1. 如果浏览器不支持 `srcset`，则 `src` 所定义的图片将会被使用。
 2. 如果浏览器支持 `srcset` ，并且屏幕能够胜任两倍的分辨率，则 `srcset` 所定义的图片将会被采用
 3. 如果浏览器支持 `srcset`，但是没有足够高的分辨率，`src` 所定义的图片将会被采用（在 `srcset` 没有定义 `1x` 图片的情况下，`src` 属性会被视为这种情况下的选项）

浏览器支持是良好的，并且在飞快地改进中。只用一个属性，我们就解决了响应式图片的难题（conundrum），真棒！

最后，关于 x 描述符，值得注意的是：图片的选择是基于像素密度的。故如果一个用户将浏览器缩放至 200%（等效于将图片大小减半，将像素密度加倍），2x 图片将会被加载。这会对 无障碍访问设备（accessibility）造成一些不利（detrimental）的影响——我们当然不希望在视力受损者访问网站时加载速度下降，而仅仅是因为他们缩放了网页。

### 使用 w 描述符

w 描述符比 x 描述符稍微先进一些。w 描述符的工作原理是：对于一个特定的图片选项，它会告诉浏览器 x 轴上的实际像素有多少（即宽度）。

截止写作时，Edge，Safari 以及 iOS Safari 尚不支持 w 描述符，这在某些程度上削弱了它的实用性。

让我们回到原来的图片：

```html
<img src="image.jpg" alt="an image" />
```

假设在本地时，这张图片的宽度是 1600 像素，现在我们想要新增一张视网膜级的图片。正如 x 描述符，我们将在 `srcset` 中定义宽为一张 3200 像素的图片：

```html
<img srcset="retina-image.jpg 3200w" src="image.jpg" alt="an image" />
```

w 描述符最大的毛病（gotcha）就是：尽管在使用 x 描述符时， `src` 属性被视为默认选项，在支持 `srcset` 的浏览器上使用 w 描述符时它却会被忽略。在使用 w 描述符时，我们只能显示地定义默认图片：加上第二个 `srcset` 图片选项，用逗号分隔：

```html
<img srcset="retina-image.jpg 3200w, image.jpg 1600w" src="image.jpg" alt="an image" />
```

导致有代码洁癖的我们要去使用……

### 使用多幅图片

能够在 HTML 代码中为浏览器提供高分辨率图片选项，确实很酷——然而，就像你所猜测的那样，当我们指定多幅图片时，事情会变得更酷。

响应式图片的目的，就是为了给不同的设备提供尽可能高质量的图片，而不要存在任何冗余。简单地提供一张高质量的图片还不够，我们需要提供更多的选择——比如 1x、1.5x、2x、2.5x 和 3x 的。

再回过头来，这是我们的原始定义：

```html
<img src="image.jpg" alt="an image" />
```

接下来，我们为浏览器提供了一个视网膜级的选项：

```html
<img srcset="retina-image.jpg 2x" src="image.jpg" alt="an image" />
```

而在这一次，我们会提供更多的额外选项，我们用逗号分隔它们：

```html
<img srcset="huge-image.jpg 3x, retina-image 2x, moderate-image 1.5x" src="image.jpg" alt="an image" />
```

由于对于不同的人而言，关键字有着不同的意思，我建议根据 x 描述符来为图片命名，这样更有助于人脑的记忆，同时也更容易确定各个图片的尺寸以及让团队中的成员更加清楚：

```html
<img srcset="image_3x.jpg 3x, image_2x.jpg 2x, image_1-5.jpg 1.5x" src="image.jpg" alt="an image" />
```

要记住：我们并没有告诉浏览器应该选择哪一幅图片，我们只是将可用的选项告诉了它，并允许它自行选择。浏览器只会下载其中的一副图片。

在使用多幅图片时有一个问题：永远不要为一幅图片定义两种描述符——举个例子：

```html
<img srcset="cross-the-streams.jpg 2x, cross-the-streams.jpg 3200w" src="image.jpg" alt="an image" />
```

[这会很不好](https://www.youtube.com/watch?v=jyaLZHiJJnE)……

### 使用 sizes

除了定义格式，`sizes` 属性是相当有趣的，因为 `sizes` 属性的值是相对于 viewport 而言的，而不是图片本身。

使用 `vw` （viewport width），我们以相对于浏览器宽度的方式指定了图片区域——记住，`img` 标签现在只等效于一个占位符，因此我们不是在指定图片的实际尺寸，而是在指定包含图片的占位符的尺寸。

`100v` 就是 100% 的 viewport 宽度， `50vw` 就是 50% 的 viewport 宽度，`25vw` 就是 25% 的 viewport 宽度……以此类推。

如果我们想让 `img` 的宽度达到浏览器宽度的一半，我们可以这样：

```html
<img sizes="50vw" srcset="retina-image.jpg 2x" src="image.jpg" alt="an image" />
```

这并不是特别有用，直到我们将它和 media query 结合起来……

### 使用 media query

当我们将 `sizes` 属性和 media query 相结合时，它会变得越来越强大。我们可以用逗号分隔多个 viewport 宽度，并通过 CSS 风格的 media query 告诉浏览器该使用哪一个。

举个例子，想象我们需要这么一张图片：在大多数的设备上它将占用 80% 的浏览器宽度，但在宽度小于等于  380px 的小尺寸设备（手机）上，我们想让它充满所有的空间（100% 的宽度）。我们应该这么写：

```html
<img sizes="(max-width: 380px) 100vw, 80vw" srcset="retina-image.jpg 2x" src="image.jpg" alt="an image" />
```

根据这个逻辑，任何视口宽度小于等于 380px 的浏览器会让图片充满 100% 的视口。其他的浏览器则会导致 media query 返回 `false`，从而采用另外的值——在这个例子中，即 `80vw`。

一般说来（As a general rule），我对在 HTML 使用 media query 表示十分反感。只是因为响应式图片数据是属于 HTML 的（不是 Javascript），而 media query 却是属于 CSS 的（不是 HTML）。但是，如果你需要，这也不失为一个选择。

## 响应式图片的最佳实践（2016？）

我不知道你是怎么想的，但我确实为 `srcset` 带来的改变感到兴奋。这是一个复杂问题的一个简单的解决方案，并且似乎提供了我们所需的所有东西。

但是，就像公交车一样，你为了响应式图片的官方解决方案等待了 20 年，而且一上场就有两个。除了 `img` 标签的 `srcset` 属性，我们还有 `picture` 标签。

`picture` 标签是另外一种占位符——尽管（albeit）是较为传统的一种。它被设计为 HTML5 中 `audio` 和 `video` 标签的模仿者（mimic），因此，它的语法被大多数人所熟识。当你需要更多 `srcset` 不能提供的功能时，建议你使用 `picture`。

遗憾的是，`picture` 的浏览器支持比 `srcset` 更差，并且**它不会静默失败**。

### 使用 picture

这是图片的原始定义：

```html
<img src="image.jpg" alt="an image" />
```

这是一副嵌套在 `picture` 中的图片：

```html
<picture>
    <img src="image.jpg" alt="an image" />
</picture>
```

在 `picture` 标签中，我们也可以为 `img` 标签指定 `srcset` 属性：

```html
<picture>
    <img srcset="retina-image.jpg 2x" src="image.jpg" alt="an image" />
</picture>
```

### 使用 source 标签

在没有增加 `source` 标签时，`picture` 标签是死的：

```html
<picture>
    <source />
    <img src="image.jpg" alt="an image" />
</picture>
```

当选择所要展示的图片时，浏览器会从第一个 `source` 标签开始遍历，直到找到一个 `media` 值为 `true` 的 `source` 标签为止。该 `source` 标签的 `srcset` 属性将会被采用。

例如，我们可以为图片指定”肖像“（portrait）格式和”风景“格式：

```html
<picture>
    <source media="orientation:landscape" srcset="horizontal-image.jpg" />
    <source media="orientation:portrait" srcset="vertical-image.jpg" />
    <img src="image.jpg" alt="an image" />
</picture>
```

甚至，我们可以用 x 描述符 和 w 描述符 来指定多幅图片：

```html
<picture>
    <source media="orientation:landscape" srcset="retina-horizontal-image.jpg 2x, horizontal-image.jpg" />
    <source media="orientation:portrait" srcset="retina-vertical-image.jpg 2x, vertical-image.jpg" />
    <img src="image.jpg" alt="an image" />
</picture>
```

在 `sizes` 属性中使用 media query 时，我会质疑在 HTML 而不是在 CSS 中基于样式来控制图片的合理性。然而，如果你需要，`media` 属性也不失为一种选择。

### 使用 type

`picture` 标签真正厉害的地方，在于它能从不同的图片类型中作出选择。

想象我们现在有一张标准 PNG 图片，但我们想用 [WebP](https://developers.google.com/speed/webp/?hl=en) 格式去替换它，因为这会缩减 26% 的体积——记住，响应式图片的核心在于 用最小的数据量提供尽可能高质量的图片——然而目前它仅被 Chrome、Opera 和 Android 内置浏览器所支持。我们需要使用 `type` 属性来确定 `WebP` 格式是否被支持：

```html
<picture>
    <source type="image/webp" srcset="retina-image.webp 2x, image.webp 1x" />
    <img srcset="retina-image.jpg 2x" src="image.jpg" alt="an image" />
</picture>
```

在这个案例中，浏览器会先检查是否支持 `WebP` 格式。如果是，它会继续判断屏幕是否有足够的像素密度去显示 `retina-image,webp` 图片，如果不是，则会显示 `image.webp` 。倘若 `WebP` 不被支持，浏览器将会径直跳至 `img` 标签处并解析——这部分我们已经非常熟悉了。

`type` 属性的出现，意味着在环境支持的情况下，我们可以可以提供体积更小的图片格式。

### 已知的问题

在 IE9 中有一个已知的问题：`picture` 标签将不会静默失败。为了处理 IE9 的情况，你需要欺骗 IE9，让它以为 `source` 标签是 `video` 标签的一部分：

```html
<picture>
    <!—[if IE 9]><video style="display:none;"><![endif]—>
    <source type="image/webp" srcset="retina-image.webp 2x, image.webp 1x" />
    <!—[if IE 9]></video><![endif]—>
    <img srcset="retina-image.jpg 2x" src="image.jpg" alt="an image" />
</picture>
```

这是一个丑陋的解决方案——但聊胜于无。我们只能期望 Windows10 的发布能够加速 IE9 退出市场，因为虽然 Edge 也不支持 `picture` 标签，但至少它会用正确的方式来处理（静默失败）。

当然，也有相应的 [polyfills](https://scottjehl.github.io/picturefill/) 来实现 IE 对 `picture` 的兼容，但我的建议是去避免它。我从来不信任用 Javascript 打补丁，因为这会极大地影响性能，同时也让代码变得不可维护。

出于这种原因，我建议现在还是最好不要使用 `picture` 标签。除非，你在运营一个大规模的电子商务网站，由 `WebP` 格式节省下来的下载时间实在不足以弥补因对代码打补丁所带来的不便。

一旦 IE9 的市场份额降至 1% 以下——也许发生在明年的某一个时刻（译者注：歪果仁的看法不代表天朝的实际情况），`picture` 标签就会变得可以接受（viable）。如果你在 2016 年读到这篇文章，或许，这种方案值得你去实践。

## 创建 响应式图片

位图并不会自己放大——这点和 SVG 不一样。面对这个问题，我们的解决方法是：使用 `srcset` 或者是 `picture`，从而为不同能力的浏览器提供不同的图片。因此，我们需要提供许多种不同尺寸的图片。

许多图片编辑软件都实现了图片自动化多尺寸导出——无论使用何种软件，你都可以轻松获得各种尺寸的图片，而无需亲自逐一调整。

Adobe Photoshop 是一款事实上的（de facto）位图编辑器。尽管对于设计工作者而言，它并不是一个很好的选择，但不可否认的是——用它来设计图片确实是一种享受（smooth & reliable）。在 Photoshop 中，多图输出的实现相对直接一些：

 1. 打开图片，并将其放在一个独立的图层上。 ![](http://netdna.webdesignerdepot.com/uploads/2015/08/step_1.jpg)
 2. 将图层重命名为你要生成的文件的名字（包括扩展名）![](http://netdna.webdesignerdepot.com/uploads/2015/08/step_2.jpg)
 3. 勾选 文件 -> 生成 -> 图片资源，然后 Photoshop 会在 PSD 文件旁生成一个新目录，其中有生成好的图片。
 4. 再次重命名图层，在每个文件名前加上对应的缩放尺寸。一旦图层被重命名，对应的图片便会自动生成，因此不必重复 步骤3。![](http://netdna.webdesignerdepot.com/uploads/2015/08/step_4.jpg)

_（图片版权归 [Philip Collier](http://www.freeimages.com/photo/bikes-1447404) 所有）_

若想了解更多关于 使用 Photoshop 生成图片 的知识，请点击 (这里)[https://helpx.adobe.com/photoshop/using/generate-assets-layers.html)。

基于这些图片，我们便可以给浏览器提供 5 种选择：

```html
<img srcset="bikes_3x.jpg 3x, bikes_2-5x.jpg 2.5x, bikes_2x.jpg 2x, bikes_1-5x.jpg 1.5x" src="bikes_1x.jpg" alt="an image" />
```

## 结语

`img` 标签已经度过了漫长的 20 个春秋——或者更精确地说，在伴着缺点（inadequate）缓慢行进了 18 年后，`img` 标签在最后的两年突然“奋起直追”，直到变成今天这个相对复杂（sophisticated）的样子。

当然最重要的是：**我们找到了解决方案**。

迄今为止，在 `srcset` 和 `picture` 这两个可选项中，前者的浏览器支持相对比较完善。如果你的网站已经完成了 95%，`srcset` 的高级特性及其简洁的实现将是你的不二之选。

如果你在运营一个庞大的电子商务网站，有成千上万的产品图片需要显示，最佳的实践便是使用 WebP 格式的图片——随着 `picture` 元素的支持被不断完善，这一切的付出都是值得的。

浏览器无法依据当前的网络状况来选择适合的图片——这是现有解决方案最大的缺点。这不是我们所能左右的。在当下，我们只能祈求“好马配好鞍”了。

用最小的尺寸提供最高质量的图片，终于成为了可能。这意味着：在不久的将来，我们将能拥抱（embrace）更好的用户体验。

_（图片引用：[mountains](http://www.shutterstock.com/pic-84977458.html) & [devices](http://www.shutterstock.com/pic-116864680.html)，来自 Shutterstock）_