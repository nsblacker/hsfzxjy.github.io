title: Ubuntu 重新映射键盘布局
date: 2016-06-05 17:20:26
categories: 随手记
tags: [Key Maps, ubuntu]
---

键盘持续失灵，已经到了让我忍无可忍的地步了。

刚开始只是方向键失灵，好在可以用小键盘替代；后来右 Ctrl 和 Alt 也失灵了，好在可以用左边的替代；直到最近 Fn 键也失灵了，终于逼疯了我——因为这意味着 F1 ～ F12 都将不能使用。

我曾试图寻找方法将 CapsLock 键映射为 Fn 键映射，但失败了——Fn 键消息是由 BIOS 拦截的，无法被操作系统捕获。

但今天我找到了一个更好的替代方案：

 + 交换 Fn 和 Ctrl。这是唯一一种能让 Fn 键移位的方式，在所有的 BIOS 中都可以设置。
 + 将 CapsLock 映射为 Ctrl。反正 CapsLock 闲着也是闲着，不如用它代替坏了的键。

ubuntu 下需要执行：

```bash
setxkbmap -layout us -option ctrl:nocaps
```

参考： [How do I turn Caps Lock into an extra Control key? - Ask Ubuntu](http://askubuntu.com/questions/462021/how-do-i-turn-caps-lock-into-an-extra-control-key)
