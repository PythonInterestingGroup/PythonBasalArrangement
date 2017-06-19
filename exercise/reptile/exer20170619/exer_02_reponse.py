# -*- coding:utf-8 -*-

from urllib import request

if __name__ == "__main__":
    req = request.Request('https://github.com/UrsusMountain')
    response = request.urlopen(req)
    print("url:%s"%(response.geturl()))
    print("*****************************************************")
    print(response.info())
    print("*****************************************************")
    print("code:%s"%(response.getcode()))