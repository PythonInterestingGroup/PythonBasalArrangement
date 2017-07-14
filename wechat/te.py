# coding:utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
import time

options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
html = driver.page_source
bf1 = BeautifulSoup(html, 'lxml')
result = bf1.find_all(class_='rtcspage')
# print(result)
bf2 = BeautifulSoup(str(result[0]), 'lxml')
# print(bf2)
# print(bf2.find_all(class_='doc_title'))
# print(bf2.div.div.div.string)
#title = bf2.div.div.h1.string
title = bf2.div.div.div.string
pagenum = bf2.find_all(class_='size')
print(pagenum)
pagenum = BeautifulSoup(str(pagenum), 'lxml')
print(pagenum)
pagenum=pagenum.p.span.get_text()
print(pagenum)
# pagepattern = re.compile('页数：(\d+)页')
# print('here')
# print(pagepattern)
# num = int(pagepattern.findall(pagenum)[0])
# print('文章标题：%s' % title)
# print('文章页数：%d' % num)

