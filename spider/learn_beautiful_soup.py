# -*- coding: utf-8 -*-
#author dm

#http://blog.csdn.net/c406495762/article/details/71158264
#Beautiful Soup是python的一个库，最主要的功能是从网页抓取数据
#pip3 install beautifulsoup4
#http://beautifulsoup.readthedocs.io/zh_CN/latest/

from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>Jack_Cui</title>
</head>
<body>
<p class="title" name="blog"><b>My Blog</b></p>
<li><!--注释--></li>
<a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
</body>
</html>
"""
#使用解析的页面获得html信息，创建Beautiful Soup对象
soup=BeautifulSoup(html,'lxml')

#使用本地HTML文件来创建对象
#soup = BeautifulSoup(open(test_beautifullsoup.html),'lxml')

#格式化输出
print(soup.prettify())
print('*********')
#Beautiful Soup四大对象
#1.Tag 标签,soup加标签名轻松地获取这些标签的内容
print(soup.title)
print('*********')
print(soup.head)
print('*********')
print(soup.a)
print('*********')
print(soup.p)
print(type(soup.title))  #<class 'bs4.element.Tag'>
print('*********')
#Tag，有两个重要的属性：name和attrs
print(soup.name)
print(soup.title.name)
print('*********')
# a标签的所有属性
print(soup.a.attrs) #{'href': 'http://blog.csdn.net/c406495762/article/details/58716886', 'class': ['sister'], 'id': 'link1'}
print(soup.a['class'])  #获取a标签的class叫什么
print(soup.a.get('class'))

#2.NavigableString,获取标签内部的文字
print('*********')
print(soup.title.string)

#(3)BeautifulSoup,表示的是一个文档的全部内容.以把它当作 Tag 对象，是一个特殊的 Tag
print('*********')
print(type(soup.name))
print(soup.name)
print(soup.attrs)

#(4)Comment,是一个特殊类型的NavigableString对象，其实输出的内容仍然不包括注释符号
print('*********')
print(soup.li)
print(soup.li.string)
print(type(soup.li.string))  #<class 'bs4.element.Comment'>
from bs4 import element
if type(soup.li.string) == element.Comment:
    print(soup.li.string)
print('*********')

#c)遍历文档数
#(1)直接子节点(不包含孙节点)
#tag的content属性可以将tag的子节点以列表的方式输出：
print(soup.body.contents)
print(soup.body.contents[1])
for child in soup.body.children:
    print(child)
print('*********')
#(2)搜索文档树
#find_all(name, attrs, recursive, text, limit, **kwargs):
#find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件。
#name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉。
print(soup.find_all('a'))  #查找文档中所有的<a>标签：
#正则：找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# 如果传入列表参数，Beautiful Soup会将与列表中任一元素匹配的内容返回，下面代码找到文档中所有<title>标签和<b>标签：
print(soup.find_all(['title','b']))
#True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点
for tag in soup.find_all(True):
    print(tag.name)
print('######')
# attrs 参数定义一个字典参数来搜索包含特殊属性的tag。
print(soup.find_all(attrs={"class":"title"}))
# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False。
# 通过 text 参数可以搜搜文档中的字符串内容，与 name 参数的可选值一样, text 参数接受字符串 , 正则表达式 , 列表, True。
print(soup.find_all(text="Python3网络爬虫(三)：urllib.error异常"))
#limit 参数限制返回结果的数量
print(soup.find_all("a", limit=2))
#如果传入 class 参数,Beautiful Soup 会搜索每个 class 属性为 title 的 tag 。kwargs 接收字符串，正则表达式
print(soup.find_all(class_="title"))
