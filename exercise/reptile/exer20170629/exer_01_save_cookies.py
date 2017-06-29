# -*- coding: UTF-8 -*-

from urllib import request
from http import cookiejar

if __name__ == '__main__':

    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(filename)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')

    # cookie.save的参数说明：
    #  ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
    #  ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入。
    cookie.save(ignore_discard=True, ignore_expires=True)

