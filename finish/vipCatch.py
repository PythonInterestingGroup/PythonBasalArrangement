#!/usr/bin/Python
# coding=utf-8
import os
import requests
from lxml import html
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def getAiqiyi(url):
    response = requests.get(url).content
    selector = html.fromstring(response)
    hrefs = selector.xpath(u'//span')
    for href in hrefs:
        json=href.text
        # print json
        if json and "密码" in json and "账号" in json:
            print json

def getXunlei(url,fo):
    response = requests.get(url).content
    selector = html.fromstring(response)
    hrefs = selector.xpath(u'//font')
    # fo=open('vip.txt','w')
    for href in hrefs:
        json=href.text
        if json and "迅雷会员账号" in json and "密码" in json:
            if len(json)<50:
                print json
                fo.write(json+'\n')

def getyouku(url):
    response = requests.get(url).content
    selector = html.fromstring(response)
    hrefs = selector.xpath(u'//span')
    for href in hrefs:
        json=href.text
        # print json
        if json and "密码" in json and "账号" in json:
            print json


def getAcountArr(url):
    print 'url->'+url
    response = requests.get(url).content
    selector = html.fromstring(response)
    hrefs = selector.xpath('//a[@class="thumbnail"]/@href')
    for href in hrefs:
        print href
        getyouku(href)

def getXunleiAcountArr(url):
    print 'url->'+url
    response = requests.get(url).content
    selector = html.fromstring(response)
    # hrefs = selector.xpath('/div[id="frameJyizy5_center"]//a[@target="_blank"]/@href')
    hrefs = selector.xpath('//div[@class="module cl xl xl1"]//a/@href')
    path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
    fo=open('%s/XLvip.txt'%(path),'w')
    for href in hrefs:
        if "thread" in href:
            # print href
            getXunlei(href,fo)
    fo.close()


        # getXunlei(href)

if __name__ == '__main__':
    # getAcountArr('http://vip.vipfenxiang.com/iqiyi/')
    # getAcountArr('http://vip.vipfenxiang.com/yk/')

    # getXunlei('http://521xunlei.com/thread-18618-1-1.html')
    

    getXunleiAcountArr('http://521xunlei.com/portal.php')

