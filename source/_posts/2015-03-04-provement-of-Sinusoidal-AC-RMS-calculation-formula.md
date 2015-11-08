---
layout: post
title: 关于正弦交流电有效值计算公式的证明
date: 2015-03-04 19:32:50.000000000 +08:00
categories:
- 数学
tags:
- 物理
---

### 公式

$I = {I_m \over \sqrt{2}}$

### 证明

设 $I = Asin\omega t$，则$I^2 = A^2sin^2\omega t$。

取半个周期进行计算：$${Q \over R} $$  
$$= \int\_0^{T \over 2} I^2tdt$$  
$$={A^2 \over 2}(t - {sin2\omega t \over 2\omega})|\_{0}^{T \over 2}$$  
$$={A^2T \over 4}$$  
$$={I^2T \over 2}$$

进而： $I = {A \over \sqrt{2}}$
