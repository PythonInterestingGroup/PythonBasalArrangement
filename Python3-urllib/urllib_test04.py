# _*_ coding:utf-8

from urllib import request

if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    # html = response.read()
    print("geturl :%s"%(response.geturl()))
    print("*****************************")
    print("info :%s"%(response.info()))
    print("*****************************")
    print("getcode :%s" % (response.getcode()))
