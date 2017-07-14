# -*- coding: utf-8 -*-
#author dm
#http://blog.csdn.net/c406495762/article/details/72597755

#官方中文教程：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
#使用requests第三方库，这个库可不是Python3内置的urllib.request库，而是一个强大的基于urllib3的第三方库。
#pip3 install requests

#爬取《帅啊》网的帅哥图片！ URL : http://www.shuaia.net/index.html

# 获取第一页所有图片地址
#目标的地址存储在class属性为”item-img”的<a>标签的href属性中
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'http://www.shuaia.net/index.html'
    headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    req = requests.get(url = url,headers = headers)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    targets_url = bf.find_all(class_='item-img')
    print(targets_url)
    list_url = []
    for each in targets_url:
        list_url.append(each.img.get('alt') + '=' + each.get('href'))
    print(list_url)

#爬取多页目标连接
#翻到第二页的时候，很容易就发现地址变为了:www.shuaia.NET/index_2.html。第三页、第四页、第五页依此类推。
if __name__ == '__main__':
    list_url = []
    for num in range(1,20):  #爬取19页图片链接
        if num == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % num
        headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url = url,headers = headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='item-img')

        for each in targets_url:
            list_url.append(each.img.get('alt') + '=' + each.get('href'))
    print(list_url)

#单张图片下载
#进入目标地址，审查元素。可以看到，图片地址保存在了class属性为”wr-single-content-list “的div->div->img的src属性中。
import os
import urllib
import re
'''
target_url = 'http://www.shuaia.net/rihanshuaige/2017-05-18/1294.html'
filename = '张根硕拍摄机车型男写真帅气十足' + '.jpg'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
img_req = requests.get(url = target_url,headers = headers)
img_req.encoding = 'utf-8'
img_html = img_req.text
img_bf_1 = BeautifulSoup(img_html, 'lxml')
img_url = img_bf_1.find_all('div', class_='wr-single-content-list')
img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
img_url = 'http://www.shuaia.net' + img_bf_2.div.img.get('src')
if 'images' not in os.listdir():
    os.makedirs('images')
urllib.urlretrieve(url = img_url,filename = 'images/' + filename)
print('下载完成！')
'''
#下载前两页的代码
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time

if __name__ == '__main__':
    list_url = []
    for num in range(1,3):
        if num == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % num
        headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url = url,headers = headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='item-img')

        for each in targets_url:
            list_url.append(each.img.get('alt') + '=' + each.get('href'))

    print('链接采集完成')

    for each_img in list_url:
        img_info = each_img.split('=')
        target_url = img_info[1]
        filename = img_info[0] + '.jpg'
        print('下载：' + filename)
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        img_req = requests.get(url = target_url,headers = headers)
        img_req.encoding = 'utf-8'
        img_html = img_req.text
        img_bf_1 = BeautifulSoup(img_html, 'lxml')
        img_url = img_bf_1.find_all('div', class_='wr-single-content-list')
        img_bf_2 = BeautifulSoup(str(img_url), 'lxml')
        img_url = 'http://www.shuaia.net' + img_bf_2.div.img.get('src')
        if 'images' not in os.listdir():
            os.makedirs('images')
        urlretrieve(url = img_url,filename = 'images/' + filename)
        time.sleep(1)

    print('下载完成！')