# -*- coding: utf-8 -*-
#author dm
#http://blog.csdn.net/c406495762/article/details/72331737

#爬取百度文库文章
#使用User-Agent，模拟手机登录，然后打印文章标题，文章页数，并进行翻页
'''
from selenium import webdriver
#自动翻页
options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(chrome_options = options)
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
page = driver.find_elements_by_xpath("//div[@class='page']") #页数
driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去
nextpage = driver.find_element_by_xpath("//a[@data-fun='next']")
nextpage.click()

#用beautifulsoup爬取当前页面内容
from selenium import webdriver
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')

html = driver.page_source
bf1 = BeautifulSoup(html, 'lxml')
result = bf1.find_all(class_='rtcspage')
for each_result in result:
     bf2 = BeautifulSoup(str(each_result), 'lxml')
     texts = bf2.find_all('p')
     for each_text in texts:
          main_body = BeautifulSoup(str(each_text), 'lxml')
          for each in main_body.find_all(True):
               if each.name == 'span':
                    print(each.string.replace('\xa0',''),end='')
                elif each.name == 'br':
                    print('')
'''

#整合代码：
#思路：爬取正文内容，再根据爬取到的文章页数，计算页数/5.0，得到一个分数，如果这个分数大于1，则翻页继续爬，如果小于或等于1，代表到最后一页了。停止翻页。有一点注意一下，翻页之后，等待延时一下，等待页面加载之后在爬取内容，这里，我们使用最简单的办法，用sleep()进行延时。
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')

    html = driver.page_source
    bf1 = BeautifulSoup(html, 'lxml')
    result = bf1.find_all(class_='rtcspage')
    bf2 = BeautifulSoup(str(result[0]), 'lxml')
    print(bf2)
    print(bf2.find_all(class_='doc_title'))
    print(bf2.div.div.div.string)
    #title = bf2.div.div.h1.string
    title = bf2.div.div.div.string
    #'''
    pagenum = bf2.find_all(class_='size')
    print(pagenum)
    pagenum = BeautifulSoup(str(pagenum), 'lxml')
    print(pagenum)
    pagenum=pagenum.span.get_text()
    print(pagenum)
    pagepattern = re.compile('(\d+)页')
    print(pagepattern)
    num = int(pagepattern.findall(pagenum)[0])
    #'''
    #num=6
    print('文章标题：%s' % title)
    print('文章页数：%d' % num)

    while True:
        num = num / 5.0
        html = driver.page_source
        bf1 = BeautifulSoup(html, 'lxml')
        result = bf1.find_all(class_='rtcspage')
        for each_result in result:
            bf2 = BeautifulSoup(str(each_result), 'lxml')
            texts = bf2.find_all('p')
            for each_text in texts:
                main_body = BeautifulSoup(str(each_text), 'lxml')
                for each in main_body.find_all(True):
                    if each.name == 'span':
                        print(each.string)
                        print(each.string.replace('\xa0', ''),end='')
                    elif each.name == 'br':
                        print('')
            print('\n')
        if num > 1:
            page = driver.find_elements_by_xpath("//div[@class='page']")
            driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去
            nextpage = driver.find_element_by_xpath("//a[@data-fun='next']")
            nextpage.click()
            time.sleep(3)
        else:
            break
