#!/usr/bin/env python
#-*- coding:utf-8 -*-

from urllib import request
from urllib import error
# HTTPError异常
if __name__ == '__main__':
    req = request.Request("http://www.douyu.com/jx_deng.html")
    try:
        response = request.urlopen(req)
        html = response.read().ecode('utf-8')
        print(html)
    except error.HTTPError as e:
        print(e.code)
    # www.douyu.com这个服务器是存在的，但是我们要查找的jx_deng.html资源是没有的，所以抛出404异常