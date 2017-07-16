from bs4 import BeautifulSoup
from bs4 import element
import re

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
soup = BeautifulSoup(html, 'lxml')

# 遍历
## 直接子节点(不包括孙节点)
### contents
print('------------- contents ---------------')
bodyContents = soup.body.contents
print("bodyContents: ", str(bodyContents))
print("bodyContents[1]: ", bodyContents[1])
print("""
""")
### children
print('------------- children ---------------')
bodyChildren = soup.body.children
for index, child in enumerate(bodyChildren):
    print("child%s :" % str(index), child)

print("""
""")
## 搜索文档树
## find_all(name, attrs, recursive, text, limit, **kwargs)：
### name
#### 传递字符
print('------------- find_all ---------------')
print('* find_all(name, attrs, recursive, text, limit, **kwargs)：')
print('** name')
print('1. 传递字符:')
tag_a = soup.find_all('a')
print("type(soup.find_all('a'))",type(tag_a))
print("")
for index, child in enumerate(tag_a):
    print("a%s :" % str(index), child)

print("""
""")
#### 传递正则
print('2. 传递正则:')
tag_re = soup.find_all(re.compile('^[a-g]{1}$'))
print("type(soup.find_all(re.compile('[a-g]{1}')))",type(tag_re))
print("type(soup.find_all(re.compile('[a-g]{1})[0]", type(tag_re[0]))

print("")
for index, child in enumerate(tag_re):
    print("<%s> :" % child.name, child)

print("""
""")

#### 传递列表
print('3. 传递列表:')
tag_list = soup.find_all(['title','li','b'])
for index, child in enumerate(tag_list):
    print("<%s> :" % child.name, child)

print("""
""")

#### 传递True：
print('4. 传递True:')
for tag in soup.find_all(True):
    print(tag.name)
print("""
""")

print('** attrs')
for tag in soup.find_all(attrs={"class":"title"}):
    print(tag)
print("""
""")

print('** recursive')
print('** text')
print('** limit')
print('** kwargs')