#! /usr/bin/env python
#  -*- coding:UTF-8 -*-

from urllib import request
from urllib import error
import chardet
from bs4 import BeautifulSoup

## 爬取目录
def crawling_catalogue(base_url, path, novel_name):
    print('正在爬取<<' + novel_name + '>>章节目录...')

    url = base_url + path
    try:
        response = request.urlopen(url)
        content_bytes = response.read()
        charset = chardet.detect(content_bytes)
        coding = charset.get('enconding', 'utf-8')
        content_string = content_bytes.decode(coding, 'ignore')
    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError\n",'ErrorCode:',e.code)
        elif hasattr(e, 'reason'):
            print("URLError\n",'ErrorReason:',e.reason)

    print("Response:")
    print("url:%s" % (response.geturl()))
    print("-----------------------------------------------------")
    print(response.info())
    print("code:%s" % (response.getcode()))
    print('charset:', charset.get('encoding', 'utf-8'))
    print("-----------------------------------------------------")

    html_soup = BeautifulSoup(content_string, 'lxml')
    catalogue_soup = BeautifulSoup(str(html_soup.find_all(id='list')), 'lxml')

    # 去除<dt>标签
    for s in catalogue_soup('dt'):
        s.extract()

    index = 0
    charter_urls = []
    charter_titles = []

    with open(novel_name + '目录.txt', 'wb') as chapter_file:
        for child in catalogue_soup.dl.children:
            if child != '\n':
                # 过滤掉前面的最新更新,为了节省时间,只爬个10章
                if index > 10 and index < 21:
                    child_url = base_url + child.a.get('href')
                    child_title = child.a.string;

                    charter_urls.append(child_url)
                    charter_titles.append(child_title)

                    chapter_file.write(child_title.encode('utf-8'))
                    chapter_file.write('\n'.encode('utf-8'))
                index += 1

    return charter_urls, charter_titles

## 爬取内容
def crawling_novel(urls, titles, novel_name):
    file = open(novel_name + '.txt', 'wb')

    for index, url in enumerate(urls):
        title = titles[index]
        print('正在爬取', ':', title, '...')

        try:
            response = request.urlopen(url)
            content_bytes = response.read()
            charset = chardet.detect(content_bytes)
            coding = charset.get('encoding', 'utf-8')
        except error.URLError as e:
            if hasattr(e, 'code'):
                print("HTTPError\n", 'ErrorCode:', e.code)
            elif hasattr(e, 'reason'):
                print("URLError\n", 'ErrorReason:', e.reason)

        content_string = content_bytes.decode(coding, 'ignore')
        html_soup = BeautifulSoup(content_string, 'lxml')
        text_soup = BeautifulSoup(str(html_soup.find_all(id='content')), 'lxml')

        # 去除内容中的 <script> 标签
        for s in text_soup('script'):
            s.extract()

        for br_tag in text_soup.find_all('br'):
            br_tag.replace_with('\n')

        content = text_soup.div.text

        file.write(title.encode('utf-8'))
        file.write('\n\n\n'.encode('utf-8'))
        file.write(content.encode('utf-8'))
        file.write('\n\n\n\n\n'.encode('utf-8'))


if __name__ == '__main__':
    base_url = 'http://www.biqudu.com'
    path = '/0_32/'
    name = '全职高手'

    urls, titles = crawling_catalogue(base_url, path, name)

    if(urls and titles and len(urls)>0 and len(titles)):
        crawling_novel(urls, titles, name)

