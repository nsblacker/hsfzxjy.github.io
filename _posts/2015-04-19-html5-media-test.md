---
title: 初试HTML5
layout: post
categories: HTML5
---

## audio & video
    
```html
<video src="http://www.w3school.com.cn/i/movie.ogg" controls="controls">
您的浏览器不支持 video 标签。
</video>
<audio src="http://www.w3school.com.cn/i/horse.ogg" controls="controls">
Your browser does not support the audio element.
</audio>
``` 

<div class="center-example">
    <video src="http://www.w3school.com.cn/i/movie.ogg" controls="controls">
    您的浏览器不支持 video 标签。
    </video>
    <audio src="http://www.w3school.com.cn/i/horse.ogg" controls="controls">
    Your browser does not support the audio element.
    </audio>
</div>

## canvas

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

<div class="center-example">
    <canvas id="myCanvas" class="align-center">
        your browser does not support the canvas tag 
    </canvas>
</div>

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

## LocalStorage

```js
var $input = $("#localstorage-input"), key = 'my-key';
$input.val(localStorage.getItem(key));
$input.on('change, keyup', function () {
    localStorage.setItem(key, $input.val());
})
```

<div class="example">
    <div class="form-group">
        <label class="control-label">这个文本框中的内容不会改变：</label>
        <input id="localstorage-input" type="text" class="form-control">
    </div>
</div>
<script type="text/javascript">
    var $input = $("#localstorage-input"), key = 'my-key';
    $input.val(localStorage.getItem(key));
    $input.on('change, keyup', function () {
        localStorage.setItem(key, $input.val());
    })
</script>