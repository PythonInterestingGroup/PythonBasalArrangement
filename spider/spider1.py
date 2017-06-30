# -*- coding: utf-8 -*-
#author dm

#https://www.baidu.com/
#protocol :// hostname[:port] / path / [;parameters][?query]#fragment
#(1)protocol：第一部分就是协议，例如百度使用的就是https协议；
#(2)hostname[:port]：第二部分就是主机名(还有端口号为可选参数)，一般网站默认的端口号为80，例如百度的主机名就是www.baidu.com，这个就是服务器的地址;
#(3)path：第三部分就是主机资源的具体地址，如目录和文件名等。

#urllib是一个URL处理包，这个包中集合了一些处理URL的模块
#urllib.request模块是用来打开和读取URLs的；
#urllib.error模块包含一些有urllib.request产生的错误，可以使用try进行捕捉处理；
#urllib.parse模块包含了一些解析URLs的方法；
#.urllib.robotparser模块用来解析robots.txt文本文件.它提供了一个单独的RobotFileParser类，通过该类提供的can_fetch()方法测试爬虫是否可以下载一个页面。

#urllib.request.urlopen()这个接口函数就可以很轻松的打开一个网站，读取并打印信息。
#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

from urllib import request
if __name__=='__main__':
    response=request.urlopen('http://fanyi.baidu.com') #返回的对象response如同一个文本对象
    html=response.read()
    html=html.decode('utf-8') #将网页的信息进行解码
    print(html)

#获取网页编码格式
#chardet.detect()方法，判断网页的编码方式
import chardet
if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)   #{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}






