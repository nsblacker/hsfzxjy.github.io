---
layout: post
title: 拉格朗日乘数法
date: 2014-12-27T08:55:52.000Z
categories:
  - 数学
tags: []
status: publish
type: post
published: true
---

> 今天在听**张心捷同学**讲题的时候，得知了一个很厉害的**在限制条件下求多远函数极值的办法**----**拉格朗日乘数法**。在这里记录一下。

# **引题**
已知：$a,b,c>0$，$a+b+c=1$。证明：$\sum\_{cyc}(1-a^2)^2\geq 2$。

# **拉格朗日乘数法的表述**
对于多值函数$y=f(x\_1,x\_2,\ldots ,x\_n)$以及约束条件$\phi(x\_1,x\_2,\ldots,x\_n)=0$，若待定一个系数$\lambda$，则由方程组：

$$\frac{\partial f}{\partial x\_1}+\lambda\cdot{\partial \phi \over \partial x\_1}=0,$$

$$\frac{\partial f}{\partial x\_2}+\lambda\cdot{\partial \phi \over \partial x\_2}=0,$$

$$\ldots$$

$$\frac{\partial f}{\partial x\_n}+\lambda\cdot{\partial \phi \over \partial x\_n}=0,$$

$$\phi(x\_1,x\_2,\ldots,x\_n)=0$$

可得一系列的解。这些解即为$y=f(x\_1,x\_2,\ldots ,x\_n)$在约束条件$\phi(x\_1,x\_2,\ldots,x\_n)=0$下可能的极值点。

# **解**
由拉格朗日乘数法，我们可解得：$(a,b,c)=(1,0,0),(0,1,0),(0,0,1)$。这是一些可能的极值点，在这些点上$f$都等于2。

当然，我们还要考虑边界情况：即$a,b,c$有一个为1或0。在这些情况下我们使用拉格朗日乘数法依旧可得上面的结论。
