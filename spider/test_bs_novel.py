# -*- coding: utf-8 -*-
#author dm

#爬取小说一念永恒并保存到文件
from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == "__main__":
    file=open('一念永恒.txt', 'w', encoding='utf-8')
    target_url = 'http://www.biqukan.com/1_1094/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req=request.Request(url=target_url,headers=head)
    target_response=request.urlopen(target_req)
    targer_html=target_response.read().decode('gbk','ignore')
    listmain_soup=BeautifulSoup(targer_html,'lxml')
    chapters = listmain_soup.find_all('div', class_='listmain')
    download_soup = BeautifulSoup(str(chapters), 'lxml')
    numbers=len(download_soup.dl.contents)
    #numbers = (len(download_soup.dl.contents) - 1) / 2 - 8 #计算章节个数  Q：为什么这么算= =
    index = 1
    begin_flag = False #开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
    # 遍历dl标签下所有子节点
    for child in download_soup.dl.children:
        # 滤除回车
        if child != '\n':
            # 找到《一念永恒》正文卷,使能标志位
            if child.string == u"《一念永恒》正文卷":
                begin_flag = True
                # 爬取链接并下载链接内容
            if begin_flag == True and child.a != None:
                download_url = "http://www.biqukan.com" + child.a.get('href')
                download_req = request.Request(url=download_url, headers=head)
                download_response = request.urlopen(download_req)
                download_html = download_response.read().decode('gbk', 'ignore')
                download_name = child.string
                soup_texts = BeautifulSoup(download_html, 'lxml')
                texts = soup_texts.find_all(id='content', class_='showtxt')
                soup_text = BeautifulSoup(str(texts), 'lxml')
                write_flag = True
                file.write(download_name + '\n\n')
                # 将爬取内容写入文件
                for each in soup_text.div.text.replace('\xa0', ''):
                    if each == 'h':
                        write_flag = False
                    if write_flag == True and each != ' ':
                        file.write(each)
                    if write_flag == True and each == '\r':
                        file.write('\n')
                file.write('\n\n')
                # 打印爬取进度
                sys.stdout.write("已下载:%.3f%%" % float(index / numbers) + '\r')
                sys.stdout.flush()
                index += 1
    file.close()
