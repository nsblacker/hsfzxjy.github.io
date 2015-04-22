---
title: 初试HTML5
layout: post
categories: HTML5
---

### audio & video
    
```html
<video src="http://www.w3school.com.cn/i/movie.ogg" controls="controls">
您的浏览器不支持 video 标签。
</video>
<audio src="http://www.w3school.com.cn/i/horse.ogg" controls="controls">
Your browser does not support the audio element.
</audio>
``` 

<div class="align-center">
    <video src="http://www.w3school.com.cn/i/movie.ogg" controls="controls">
    您的浏览器不支持 video 标签。
    </video>
    <audio src="http://www.w3school.com.cn/i/horse.ogg" controls="controls">
    Your browser does not support the audio element.
    </audio>
</div>

### Canvas

```html
<canvas id="myCanvas">
    your browser does not support the canvas tag 
</canvas>

<script type="text/javascript">
    var canvas=document.getElementById('myCanvas');
    var ctx=canvas.getContext('2d');
    ctx.fillStyle='#FF0000';
    ctx.fillRect(0,0,80,100);
    var grd=ctx.createLinearGradient(0,0,175,50);
    grd.addColorStop(0,"#FF0000");
    grd.addColorStop(1,"#00FF00");
    ctx.fillStyle=grd;
    ctx.fillRect(0,100,175,50);
</script>
```

<canvas id="myCanvas" class="align-center">
    your browser does not support the canvas tag 
</canvas>

<script type="text/javascript">
    var canvas=document.getElementById('myCanvas');
    var ctx=canvas.getContext('2d');
    ctx.fillStyle='#FF0000';
    ctx.fillRect(0,0,80,100);
    var grd=ctx.createLinearGradient(0,0,175,50);
    grd.addColorStop(0,"#FF0000");
    grd.addColorStop(1,"#00FF00");
    ctx.fillStyle=grd;
    ctx.fillRect(0,100,175,50);
</script>