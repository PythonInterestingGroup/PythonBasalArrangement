#!/user/bin/env python
#-*- coding:utf-8 -*-

from  urllib import request

if __name__ == '__main__':
    req = request.Request("http://fanyi.baidu.com")
    response = request.urlopen(req)
    print("geturl(): %s" %(response.geturl()))
    print('\n')
    print("info():%s"% (response.info()))
    print('\n')
    print("getcode():%s" % (response.getcode()))
