## Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:

## Tag
## NavigableString
## BeautifulSoup
## Comment

from bs4 import BeautifulSoup
from bs4 import element

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

## Comment
## Comment对象是一个特殊类型的NavigableString对象，其实输出的内容仍然不包括注释符号
print(soup.li)
print(soup.li.string)
print(type(soup.li.string))

if type(soup.li.string) == element.Comment:
    print(soup.li.string)





