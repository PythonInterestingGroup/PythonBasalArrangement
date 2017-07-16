#! /usr/bin/env python
#  -*- coding:UTF-8 -*-
from urllib import request
from urllib import  error
import chardet
from bs4 import BeautifulSoup


if __name__ == '__main__':

    # download_url = 'http://www.biqukan.com/1_1094/5403177.html'
    download_url = 'http://www.biqudu.com/0_32/1003682.html'
    # download_url = 'https://github.com/UrsusMountain'
    # head = {}
    # head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    # download_req = request.Request(url=download_url,headers=head)



    try:
        # download_response = request.urlopen(download_req)
        download_response = request.urlopen(download_url)
        download_stream = download_response.read()
        charset = chardet.detect(download_stream)

        print("Response:")
        print("url:%s" % (download_response.geturl()))
        print("-----------------------------------------------------")
        print(download_response.info())
        print("code:%s" % (download_response.getcode()))
        print('charset:', charset.get('encoding', 'utf-8'))
        print("-----------------------------------------------------")

        coding = charset.get('encoding', 'utf-8')
        download_html = download_stream.decode(coding,'ignore')
        htmlSoup = BeautifulSoup(download_html, 'lxml')
        # print(htmlSoup.prettify())

        textSoup = BeautifulSoup(str(htmlSoup.find_all(id = 'content')), 'lxml')
        # print(textSoup.prettify())

        # 去除内容中的 <script> 标签
        for s in textSoup('script'):
            s.extract()

        for br_tag in textSoup.find_all('br'):
            br_tag.replace_with('\n')

        content = textSoup.div.text
        print(content)

        with open('qzgs.txt','wb') as f:
            f.write(content.encode(coding))
    except error.URLError as e:
        if hasattr(e,'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e,'reason'):
            print("URLError")
            print(e.reason)


