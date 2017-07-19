#!/usr/bin/env python
#-*- coding:utf-8 -*-

from  urllib import request
from  urllib import error
# 下URLError的异常
if __name__ == '__main__':
    #一个不存在的链接
    url = "http://wwww.iloveyou.com/"
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except error.URLError as e:
        print(e.reason)