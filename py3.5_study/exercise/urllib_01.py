#!/user/bin/env python3
#-*- coding:utf-8 -*-
from urllib import request

if __name__ == '__main__':
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    print(html)