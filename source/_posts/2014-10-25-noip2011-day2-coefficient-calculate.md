---
layout: post
title: NOIP2011 Day2 计算系数：快速求组合数
date: 2014-10-25 23:27:13.000000000 +08:00
categories:
- 编程
tags:
- 数论
- 信息学竞赛
- 数学
---
## **题目大意**

> 输入a, b, k, n, m，计算$a^n\times b^m\times C_k^n$模10007的余数。

## **分析**

对于幂数的计算并不难，关键在于对组合数$C_n^k$的计算。  
通常来说，组合数的计算一般是这样的：$$C_n^k=\frac{n}{k}\times\frac{n-1}{k-1}\times\ldots\times\frac{n-k+1}{1}$$ 这对于单精度的计算来说是十分快捷的，但如果要对结果取模的话就不起作用了——**取模运算对于除法不成立**。因此只能另辟蹊径了。  
注意到**加减乘法对于取模都是成立的**，从而想到：能否将组合数转化成加法？  
自然而然，想到了组合恒等式：$$C_n^k=C_{n-1}^{k}+C_{n-1}^{k-1}$$ 思路到此完成。

## **Code**

    const
        modn = 10007;
    var
        a, b, k, m, n: longint;
        map: array[0..1000,0..1000] of int64; //缓存
    //快速幂
    function power(a, x: longint): int64;
    var
        t: longint;
    begin
        if x = 1 then
            exit(a);
        if x = 0 then
            exit(1);
        t := power(a, x shr 1);
        power := t * t mod modn;
        if odd(x) then
            power := power * a mod modn;
    end;
    //快速组合数
    function C(n, k: longint): int64;
    begin
        if map[n, k] > 0 then
            exit(map[n, k]);
        if (n <= k) or (k = 0) then
            C := 1
        else if k = 1 then
            C := n
        else
            C := (C(n-1, k)+C(n-1, k-1)) mod modn;
        map[n, k] := C;
    end;

    var
        t: longint;
        ans: int64;

    begin
        assign(input, 'main.in'); reset(input);
        assign(output, 'main.out'); rewrite(output);

        readln(a, b, k, n, m);
        a := a mod modn;
        b := b mod modn;
        ans := power(a, n);
        ans := ans * power(b, m) mod modn;
        //C(k,n)与C(k,m)是等效的，计算较小者即可
        if n > m then n := m; 
        ans := ans * C(k, n) mod modn;
        writeln(ans);

        close(input); close(output);
    end.