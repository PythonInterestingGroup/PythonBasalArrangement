#!/usr/bin/env python
#-*- coding:utf-8 -*-

from urllib import request
from urllib import error
import chardet

if __name__ == '__main__':
    req = request.Request("http://www.baidu.com/jx_deng.html")
    try:
        response = request.urlopen(req)
        # html = response.read()
        # mychardet = chardet.detect(html)
        # print(mychardet)

        # html = response.read().ecode('utf-8')
        # print(html)
    except error.HTTPError as e:
        print("HTTPError:%s" %e.code)
    except error.URLError as e:
        print("URLError:%s" % e.reason)
print("*****************************")
 # 如果不用上面的方法，也可以使用hasattr函数判断URLError含有的属性
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