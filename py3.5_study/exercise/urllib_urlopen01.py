#!/user/bin/env python
#-*- coding: utf-8 -*-
from urllib import request

if __name__ == '__main__':
    myrequest = request.Request("http://fanyi.baidu.com")
    response = request.urlopen(myrequest)
    html = response.read()
    html = html.decode("utf-8")
    print(html)
    