# -*- coding:UTF-8 -*-

from urllib import request
from http import cookiejar

if __name__ == '__main__':
    filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(filename,ignore_discard=True,ignore_expires=True)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))