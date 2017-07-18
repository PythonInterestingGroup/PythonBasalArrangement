# -*- coding: utf-8 -*-
#author dm

from urllib import request
from bs4 import BeautifulSoup
import chardet

head={}
head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
download_url='http://www.biqudu.com/0_32/1003682.html'
dowmload_req=request.Request(url=download_url,headers=head)
download_response=request.urlopen(dowmload_req)
download_html=download_response.read()
chardet_code=chardet.detect(download_html)
download_html=download_html.decode(chardet_code.get('encoding','utf-8'),'ignore')
#print(download_html)
content_soup=BeautifulSoup(download_html,'lxml')
#print(content_soup)
content=content_soup.find_all('div',id='content')
print(content)
for tag in content:
    print(tag.text)
print(type(content))
print(content[0].text)
#print(content.text)
content_soup1=BeautifulSoup(str(content),'lxml')
for s in content_soup1('script'):
    s.extract()
for br_tag in content_soup1.find_all('br'):
    br_tag.replace_with('\n')
content1=content_soup1.div.text
print(content1)

'''
print("Response:")
print("url:%s" % (download_response.geturl()))
print("-----------------------------------------------------")
print(download_response.info ())
print("code:%s" % (download_response.getcode()))
print('charset:', download_response.get('encoding', 'utf-8'))
print("-----------------------------------------------------")
'''