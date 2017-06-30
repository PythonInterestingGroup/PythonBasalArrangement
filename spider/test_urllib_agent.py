# -*- coding: utf-8 -*-
#author dm

#使用User Agent和代理IP隐藏身份

#要设置User Agent，有两种方法：
#1.在创建Request对象的时候，填入headers参数(包含User Agent信息)，这个Headers参数要求为字典；
#2.在创建Request对象的时候不添加headers参数，在创建完成之后，使用add_header()的方法，添加headers。

from urllib import request
########1
###以CSDN为例，CSDN不更改User Agent是无法访问的
if __name__=='__main__':
    url = 'http://www.csdn.net/'
    head={}
    head['User-Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
    req=request.Request(url, headers=head)
    response=request.urlopen(req)
    html=response.read().decode('utf-8')
    #print(html)
########2
if __name__ == "__main__":
    url = 'http://www.csdn.net/'
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    #print(html)

##Ip代理
#代理IP网站 http://www.xicidaili.com/
#编写代码访问http://www.whatismyip.com.tw/，该网站是测试自己IP为多少的网址，服务器会返回访问者的IP
if __name__=='__main__':
    url = 'http://www.whatismyip.com.tw/'
    proxy = {'http': '60.214.154.2:53281'}   #IP代理
    proxy_support = request.ProxyHandler(proxy)  #创建ProxyHandler
    opener = request.build_opener(proxy_support)   #创建Opener
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    request.install_opener(opener)  #安装OPener
    response = request.urlopen(url)   #使用自己安装好的Opener
    html = response.read().decode("utf-8")
    print(html)



'''
常见的user agent
1.Android
Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
2.Firefox
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0
3.Google Chrome
Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19
4.iOS
Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3
'''