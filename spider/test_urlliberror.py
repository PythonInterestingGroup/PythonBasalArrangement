# -*- coding: utf-8 -*-
#author dm

#urllib.error

from urllib import  request
from urllib import error

if __name__=='__main__':
    url='http://www.iloveyou.com/'
    req=request.Request(url)
    try:
        response=request.urlopen(req)
        html=response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)  #[Errno 11004] getaddrinfo failed  获取地址信息失败


if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.douyu.com/Jack1_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
        # html = responese.read()
    except error.HTTPError as e:
        print(e.code)  #404  请求的资源没有在服务器上找到，www.douyu.com这个服务器是存在的

#如果想用HTTPError和URLError一起捕获异常，那么需要将HTTPError放在URLError的前面，因为HTTPError是URLError的一个子类。如果URLError放在前面，出现HTTP异常会先响应URLError，这样HTTPError就捕获不到错误信息了。
'''错误
if __name__ == "__main__":
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
    except error.URLError as e:
        print(e.reason)
    except error.HTTPError as e:
        print(e.code)
'''
#正确
if __name__ == "__main__":
    url = "http://www.douyu.com/Jack_Cui2.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
    except error.HTTPError as e:
        print(e.code)
    except error.URLError as e:
        print(e.reason)

#也可以使用hasattr函数判断URLError含有的属性，如果含有reason属性表明是URLError，如果含有code属性表明是HTTPError。

if __name__ == "__main__":
    #一个不存在的连接
    url = "http://www.douyu.com/Jack_Cui.html"
    req = request.Request(url)
    try:
        responese = request.urlopen(req)
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e, 'reason'):
            print("URLError")
            print(e.reason)