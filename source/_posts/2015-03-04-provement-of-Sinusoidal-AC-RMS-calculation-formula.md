---
layout: post
title: 关于正弦交流电有效值计算公式的证明
permalink: /provement-of-Sinusoidal-AC-RMS-calculation-formula/
date: 2015-03-04 19:32:50.000000000 +08:00
categories:
- 数学
- 物理
---
<h3>公式</h3>
<p>$I = {I_m \over \sqrt{2}}$</p>
<h3>证明</h3>
<p>设 $I = Asin\omega t$，则$I^2 = A^2sin^2\omega t$。</p>
<p>取半个周期进行计算：$${Q \over R} $$<br />
$$= \int_0^{T \over 2} I^2tdt$$<br />
$$={A^2 \over 2}(t - {sin2\omega t \over 2\omega})|_{0}^{T \over 2}$$<br />
$$={A^2T \over 4}$$<br />
$$={I^2T \over 2}$$</p>
<p>进而： $I = {A \over \sqrt{2}}$</p>
