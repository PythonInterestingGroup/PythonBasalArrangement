# -*- coding: UTF-8 -*-

from urllib import request
from http import cookiejar

if __name__ == '__main__':
    #声明一个Cookiejar对象实例来保存
    cookie = cookiejar.CookieJar()
    #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    #通过CookieHandler创建opener
    opener = request.build_opener(handler)
    #此处的open方法打开网页
    try:
        response = opener.open('http://www.baidu.com')
        for item in cookie:
            print('Name = %s' % item.name)
            print('Value = %s' % item.value)
    except Exception as e:
        print(e)
