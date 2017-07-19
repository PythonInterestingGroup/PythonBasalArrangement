#!/user/bin/env python
#-*- coding:utf-8 -*-
from urllib import request
import  chardet

if __name__ == '__main__':
    response = request.urlopen("http://fanyi.baidu.com")
    html = response.read()
    mychardet = chardet.detect(html)
    print(mychardet)
