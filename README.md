<h1><b>哔哩哔哩签到程序</b></h1>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这几天学爬虫，看b站一个小哥哥视频学的，然后有一个签到很好玩，于是我也做了个，加了个界面，这个真是本人做的，界面是纯属自己手敲的。界面背景用的是上次爬取的JFla的封面哦，每次打开都显示不一样的JFla。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;把自己的实现过程记录下来吧，代码和图片材料也上传了，代码注释写的很详细，这边就做个简单介绍吧。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其实是一个很简单的小程序，首先要进入b站的签到页面，查看它的network，然后你签到，找到发生变化的那个文件，没记错的话应该是带sign的一个文件，反正试试嘛，
今天我签到过了，所以看不到了（反正我是没找到）。总之拿到网址以后，直接requests就好啦</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;然后就是写界面了，这里用的是pyqt5写的，官方中文文档 https://github.com/maicss/PyQt5-Chinese-tutorial 在这里啦，可以去看着学，非常详细。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;写完了以后可以打包成.exe文件，先 pip install pyinstaller，然后在文件目录下运行cmd，执行pyinstaller -w 你的文件.py就好了，使用介绍在这个博主这里
http://www.pyinstaller.org/ 这里要说明一下，你打包之后，背景图片可能显示不出来，这种情况只要把你用的图片文件夹放到（前提是你代码引用的当前目录文件）打包后的dist文件内与.exe同级目录就OK了。</p> 
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结果图在images文件夹里面后面那两张QQ截图。</p>
<br />
<p><b>随机显示名言功能加入</b></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这次在这个签到小程序界面加入随机显示名言功能，名言是从百度上爬取的青春名言。功能大概是，每次打开程序随机抽取一句名言显示在界面上，颜色也是随机的。代码改动如下：</p>
<div align="center"><img src="https://github.com/foreversunx/BilibiliSign/tree/master/images/up1.png" width="800" height="450" /></div>
<div align="center"><img src="https://github.com/foreversunx/BilibiliSign/tree/master/images/up2.png" width="800" height="450" /></div>
