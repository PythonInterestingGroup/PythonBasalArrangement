# -*- coding: utf-8 -*-
#author dm
#http://blog.csdn.net/c406495762/article/details/72793480

#爬虫黑科技之让你的爬虫程序更像人类用户的行为(代理IP池等)

# 除了处理网站表单，requests 模块还是一个设置请求头的利器。HTTP 的请求头是在你每次向网络服务器发送请求时，传递的一组属性和配置信息。

# Cookie信息，也可以更具实际情况填写。不过requests已经封装好了很多操作，自动管理cookie，session保持连接。我们可以先访问某个目标网站，建立一个session连接之后，获取cookie
# 使用 requests.Session 会话对象让你能够跨请求保持某些参数，它也会在同一个 Session 实例发出的所有请求之间保持 cookie， 期间使用 urllib3 的 connection pooling 功能
#http://docs.python-requests.org/zh_CN/latest/user/advanced.html
'''
import requests

if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    headers = {'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    }
    s = requests.Session()
    req = s.get(url=url,headers=headers)
    print(s.cookies)

#PhantomJS 是一个“无头”（headless）浏览器。它会把网站加载到内存并执行页面上的 javascript，但不会向用户展示网页的图形界面。将 Selenium 和 PhantomJS 结合在一起，就可以运行一个非常强大的网络爬虫了，可以处理 cookie、JavaScript、headers，以及任何你需要做的事情。
#下载地址：http://phantomjs.org/download.html

#，对 http://pythonscraping.com 网站调用 webdriver 的 get_cookie()方法来查看 cookie。可以获得一个非常典型的 Google Analytics 的 cookie 列表：
#还可以调用 delete_cookie()、add_cookie() 和 delete_all_cookies() 方法来处理 cookie。另外，还可以保存 cookie 以备其他网络爬虫使用。
from selenium import webdriver
if __name__ == '__main__':
    url = 'http://pythonscraping.com'
    driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())

#每个页面访问增加一点儿时间间隔
# import time
#time.sleep(1)

# 下面的例子所用的网页在 http://pythonscraping.com/pages/itsatrap.html，这是一个给我们python爬虫学习的一个网站。这个页面包含了两个链接，一个通过 CSS 隐含了，另一个是可见的。
#这三个元素通过三种不同的方式对用户隐藏：
#第一个链接是通过简单的 CSS 属性设置 display:none 进行隐藏；
#电话号码字段 name=”phone” 是一个隐含的输入字段；
#邮箱地址字段 name=”email” 是将元素向右移动 50 000 像素（应该会超出电脑显示器的边界）并隐藏滚动条。

#通过 is_displayed() 可以判断元素在页面上是否可见。

from selenium import webdriver
if __name__ == '__main__':
    url = 'http://pythonscraping.com/pages/itsatrap.html'
    driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        if not link.is_displayed():
            print('连接:' + link.get_attribute('href') + ',是一个蜜罐圈套.')

    fields = driver.find_elements_by_tag_name('input')
    for field in fields:
        if not field.is_displayed():
            print('不要改变' + field.get_attribute('name') + '的值.')


#创建自己的代理IP池
# 思路：通过免费IP代理网站爬取IP，构建一个容量为100的代理IP池。从代理IP池中随机选取IP，在使用IP之前，检查IP是否可用。如果可用，使用该IP访问目标页面，如果不可用，舍弃该IP。当代理IP池中IP的数量小于20的时候，更新整个代理IP池，即重新从免费IP代理网站爬取IP，构建一个新的容量为100的代理IP池。
#爬取国内高匿代理，第一页的URL为：www.xicidaili.com/nn/1，第二页的URL为：www.xicidaili.com/nn/2，其他页面一次类推，一页IP正好100个
#通过审查元素可知，这些ip都存放在了id属性为ip_list的table中。

import requests
from bs4 import BeautifulSoup
from lxml import etree

if __name__ == '__main__':
    #requests的Session可以自动保持cookie,不需要自己维护cookie内容
    page = 1
    S = requests.Session()
    target_url = 'http://www.xicidaili.com/nn/%d' % page
    target_headers = {'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':'http://www.xicidaili.com/nn/',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
    }
    target_response = S.get(url = target_url, headers = target_headers)
    target_response.encoding = 'utf-8'
    target_html = target_response.text
    bf1_ip_list = BeautifulSoup(target_html, 'lxml')
    bf2_ip_list = BeautifulSoup(str(bf1_ip_list.find_all(id = 'ip_list')), 'lxml')
    ip_list_info = bf2_ip_list.table.contents

    proxys_list = []
    for index in range(len(ip_list_info)):
        if index % 2 == 1 and index != 1:
            dom = etree.HTML(str(ip_list_info[index]))
            ip = dom.xpath('//td[2]')
            port = dom.xpath('//td[3]')
            protocol = dom.xpath('//td[6]')
            proxys_list.append(protocol[0].text.lower() + '#' + ip[0].text + '#' + port[0].text)
    print(proxys_list)

#如何验证这个IP是否可用呢？一种方案是GET请求一个网页，设置timeout超时间，如果超时服务器没有反应，说明IP不可用
#二：在Windows下，可以在CMD中输入如下指令查看IP的连通性(mac和Linux可以在中断查看)： Subprocess.Popen()可以创建一个进程，当shell参数为true时，程序通过shell来执行：
#ping本机回环地址
import subprocess as sp

if __name__ == '__main__':
    cmd = "ping -n 3 -w 3 127.0.0.1"
    #执行命令
    p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    #获得返回结果并解码
    out = p.stdout.read().decode("gbk")
    print(out)
'''
#如果丢包数大于2个，则认为ip不能用。ping通的平均时间大于200ms也抛弃。当然，我这个要求有点严格，可以视情况放宽规则：
from bs4 import BeautifulSoup
import subprocess as sp
from lxml import etree
import requests
import random
import re

"""
函数说明:获取IP代理
Parameters:
    page - 高匿代理页数,默认获取第一页
Returns:
    proxys_list - 代理列表
Modify:
    2017-05-27
"""
def get_proxys(page = 1):
    #requests的Session可以自动保持cookie,不需要自己维护cookie内容
    S = requests.Session()
    #西祠代理高匿IP地址
    target_url = 'http://www.xicidaili.com/nn/%d' % page
    #完善的headers
    target_headers = {'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer':'http://www.xicidaili.com/nn/',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
    }
    #get请求
    target_response = S.get(url = target_url, headers = target_headers)
    #utf-8编码
    target_response.encoding = 'utf-8'
    #获取网页信息
    target_html = target_response.text
    #获取id为ip_list的table
    bf1_ip_list = BeautifulSoup(target_html, 'lxml')
    bf2_ip_list = BeautifulSoup(str(bf1_ip_list.find_all(id = 'ip_list')), 'lxml')
    ip_list_info = bf2_ip_list.table.contents
    #存储代理的列表
    proxys_list = []
    #爬取每个代理信息
    for index in range(len(ip_list_info)):
        if index % 2 == 1 and index != 1:
            dom = etree.HTML(str(ip_list_info[index]))
            ip = dom.xpath('//td[2]')
            port = dom.xpath('//td[3]')
            protocol = dom.xpath('//td[6]')
            proxys_list.append(protocol[0].text.lower() + '#' + ip[0].text + '#' + port[0].text)
    #返回代理列表
    return proxys_list

"""
函数说明:检查代理IP的连通性
Parameters:
    ip - 代理的ip地址
    lose_time - 匹配丢包数
    waste_time - 匹配平均时间
Returns:
    average_time - 代理ip平均耗时
Modify:
    2017-05-27
"""
def check_ip(ip, lose_time, waste_time):
    #命令 -n 要发送的回显请求数 -w 等待每次回复的超时时间(毫秒)
    cmd = "ping -n 3 -w 3 %s"
    #执行命令
    p = sp.Popen(cmd % ip, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, shell=True)
    #获得返回结果并解码
    out = p.stdout.read().decode("gbk")
    #丢包数
    lose_time = lose_time.findall(out)
    #当匹配到丢失包信息失败,默认为三次请求全部丢包,丢包数lose赋值为3
    if len(lose_time) == 0:
        lose = 3
    else:
        lose = int(lose_time[0])
    #如果丢包数目大于2个,则认为连接超时,返回平均耗时1000ms
    if lose > 2:
        #返回False
        return 1000
    #如果丢包数目小于等于2个,获取平均耗时的时间
    else:
        #平均时间
        average = waste_time.findall(out)
        #当匹配耗时时间信息失败,默认三次请求严重超时,返回平均好使1000ms
        if len(average) == 0:
            return 1000
        else:
            #
            average_time = int(average[0])
            #返回平均耗时
            return average_time

"""
函数说明:初始化正则表达式
Parameters:
    无
Returns:
    lose_time - 匹配丢包数
    waste_time - 匹配平均时间
Modify:
    2017-05-27
"""
def initpattern():
    #匹配丢包数
    lose_time = re.compile(u"丢失 = (\d+)", re.IGNORECASE)
    #匹配平均时间
    waste_time = re.compile(u"平均 = (\d+)ms", re.IGNORECASE)
    return lose_time, waste_time

if __name__ == '__main__':
    #初始化正则表达式
    lose_time, waste_time = initpattern()
    #获取IP代理
    proxys_list = get_proxys(1)

    #如果平均时间超过200ms重新选取ip
    while True:
        #从100个IP中随机选取一个IP作为代理进行访问
        proxy = random.choice(proxys_list)
        split_proxy = proxy.split('#')
        #获取IP
        ip = split_proxy[1]
        #检查ip
        average_time = check_ip(ip, lose_time, waste_time)
        if average_time > 200:
            #去掉不能使用的IP
            proxys_list.remove(proxy)
            print("ip连接超时, 重新获取中!")
        if average_time < 200:
            break

    #去掉已经使用的IP
    proxys_list.remove(proxy)
    proxy_dict = {split_proxy[0]:split_proxy[1] + ':' + split_proxy[2]}
    print("使用代理:", proxy_dict)

#https://github.com/Jack-Cherish/python-spider
#《Python网络数据采集》
