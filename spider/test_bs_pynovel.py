# -*- coding: utf-8 -*-
#author dm

#beautiful_soup 单章小说爬取
#爬取URL：http://www.biqukan.com/1_1094/5403177.html

#文章的内容存放在id为content，class为showtxt的div标签中：

from urllib import request
from bs4 import BeautifulSoup
import re
if __name__ == "__main__":
    download_url = 'http://www.biqukan.com/1_1094/5403177.html'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req = request.Request(url = download_url, headers = head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk','ignore')#忽略非法字符，将gbk解码成unico,网站为gbk编码
    soup_texts = BeautifulSoup(download_html, 'lxml') #创建bs对象
    texts = soup_texts.find_all(id = 'content', class_ = 'showtxt') #找到对应标签
    soup_text = BeautifulSoup(str(texts), 'lxml') #获取标签内容
    print(soup_text.div.text.replace('\xa0', ''))
    #print(soup_text.div.Text.replace('\xa0', ' '))   #将\xa0无法解码的字符删除  gbk无法解码\xa0 报错
    #print(soup_text.text.replace('\xa0', ''))



    ####报错啦 待解决