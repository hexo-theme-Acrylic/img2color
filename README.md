## img2color PHP API
这段代码是一个PHP脚本，用于获取图片的主题色。它的主要功能如下：
- 定义了一个函数getImageThemeColor()，用于获取图片的主题色。
- 通过$_GET['img']获取传入的图片URL参数。
- 检查是否已经存在对应链接的色彩信息，如果存在则直接读取已存储的色彩信息并输出。
- 如果不存在对应链接的色彩信息，则调用getImageThemeColor()函数获取图片主题色。
- 将色彩信息存储到数组中，并将数组转换为JSON格式并存储到文件中。
- 输出JSON格式的结果，包含图片的主题色信息。

> 这边目前是我个人使用,所以色彩数据通过json存储,但是数据如果很庞大还是会吃不消,所以近期推出mysql方案
适用于[Acrylic-Pro主题](https://github.com/hexo-theme-Acrylic/hexo-theme-Acrylic)的提取主题色

## 跨域解决
> 原则上“Access-Control-Allow-Origin”这里后面不要写*，写指定域名会安全点
打开宝塔网站的配置文件,添加一下内容
```code
    add_header 'Access-Control-Allow-Origin'   '*';
    add_header 'Access-Control-Allow-Credentials'   'true';
    add_header 'Access-Control-Allow-Methods'  'GET, POST, OPTIONS';
```
