#!/usr/bin/env python3
#--*-- coding:UTF-8 --*--
from  urllib import request
if __name__ == '__main__':
    respose = request.urlopen("http://fanyi.baidu.com")
    html = respose.read()
    print (html)

