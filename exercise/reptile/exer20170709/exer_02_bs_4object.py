## Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

## Tag
## NavigableString
## BeautifulSoup
## Comment

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
soup = BeautifulSoup(html,'lxml')
# 查找标签的内容,返回的是查到的第一个
print('==========html==========')
print(soup.html)
print('==========head=========')
print(soup.head)
print('==========title=========')
print(soup.title)
print('==========a=========')
print(soup.a)
print('==========p=========')
print(soup.p)
print('======================')
print('name:')
print(soup.name)
print(soup.title.name)
print('======================')
print('attrs:')
## 返回一个集合(set)
print(soup.a['class'])
print(soup.a.attrs)
print(soup.a.get('href'))
# print(soup.a.get('herf'))
print(soup.a['id'])
print(soup.p.get('class')[0])
print('=====================')
print('NavigableString')
print(soup.title.string)


