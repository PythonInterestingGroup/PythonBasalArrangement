# -*- coding: utf-8 -*-
#author dm

from urllib import request
from bs4 import BeautifulSoup
import chardet

if __name__=="__main__":
    file = open('全职高手.txt', 'w', encoding='utf-8')
    target_url='http://www.biqudu.com/0_32/'
    head={}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req=request.Request(url=target_url,headers=head)
    response=request.urlopen(req)
    target_html=response.read()
    chardet_code=chardet.detect(target_html)
    print(chardet_code)
    target_html=target_html.decode(chardet_code.get('encoding','utf-8'),'ignore')
    soup=BeautifulSoup(target_html,'lxml')
    chapters=soup.find_all('div',id='list')
    #print(chapters)
    title=soup.h1.string
    print(title)
    file.write(title + '\n\n')
    download_soup=BeautifulSoup(str(chapters),'lxml')
    #print(download_soup)
    start=False
    index=0
    for child in download_soup.dl.children:
        #print(child)
        if child!='\n':
            if child.string=='《全职高手》第一卷':
                start=True

            if start==True and child.a!=None and index<10:
                #print(child.a.get('href'))
                download_url="http://www.biqudu.com"+child.a.get('href')
                download_name=child.text
                #print(download_name,download_url)
                dowmload_req=request.Request(url=download_url,headers=head)
                download_response=request.urlopen(dowmload_req)
                download_html=download_response.read()
                download_html=download_html.decode(chardet_code.get('encoding','utf-8'),'ignore')
                content_soup=BeautifulSoup(download_html,'lxml')
                content=content_soup.find_all(id='content')
                text_soup=BeautifulSoup(str(content),'lxml')
                for s in text_soup('script'):
                    s.extract()
                for br_tag in text_soup.find_all('br'):
                    br_tag.replace_with('\n')
                text=text_soup.div.text
                #print(download_name+text)
                print('正在下载：'+ download_name)
                file.write(download_name)
                file.write('\n\n')
                file.write(text)
                file.write('\n\n')
                index += 1
    print('下载完成！')
    file.close()








