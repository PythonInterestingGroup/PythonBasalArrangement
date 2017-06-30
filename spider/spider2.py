# -*- coding: utf-8 -*-
#author dm

from urllib import request
if __name__=="__main__":
    #response = request.urlopen('http://fanyi.baidu.com')

    req=request.Request("http://fanyi.baidu.com/")
    response=request.urlopen(req)

    print('geturl打印信息：%s'%(response.geturl())) #返回的是一个url的字符串；
    print("info打印信息：%s"%(response.info()))   #返回的是一些meta标记的元信息，包括一些服务器的信息；
    print("getcode打印信息：%s"%(response.getcode()))  #返回的是HTTP的状态码，如果返回200表示请求成功。

    html=response.read()
    html=html.decode("utf-8")
    #print(html)


