# coding:utf-8
import re
import requests
# 获取网页内容
r = requests.get('http://www.ttmeiju.com/')
data = r.text
# 利用正则查找所有连接
link_list =re.findall(r"(?<=href=\").+?(?=\")" ,data)
# print link_list
urlList=[]
def  getUrl(url):
	r = requests.get(url)
	data = r.text
	link_list =re.findall(r"(?<=href=\").+?(?=\")" ,data)
	return link_list


for url in link_list:
    if '/seed/' in url:
    	newUrl='http://www.ttmeiju.com/'+url
    	# print newUrl
    	seedUrl=getUrl(newUrl);
        for url in seedUrl:
            if '/meiju/' in url:
                pass
                url='http://www.ttmeiju.com/'+url
                # print url
                urlList.append(url)
    if '/meiju/' in url:
    	newUrl='http://www.ttmeiju.com/'+url
    	# print newUrl
    	urlList.append(newUrl)
#去重
newList=[]
for  signleUrl in urlList:
    # print signleUrl
    if signleUrl not in newList:
        newList.append(signleUrl)
# for signleUrl in newList:
#     print signleUrl
urlList=list(set(urlList))
for signleUrl in urlList:
    print signleUrl


# if __name__ == '__main__':
# 	urlList=getUrl('http://www.ttmeiju.com/')

