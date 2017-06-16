# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
import shutil
from lxml import html
reload(sys)
sys.setdefaultencoding('utf8')

	
def searchMovie(mName):
	url='http://www.ttmeiju.com/index.php/search/index.html?keyword=%s&range=0'%mName
	# print url
	response=requests.get(url).content
	selector = html.fromstring(response)
	# hrefs=selector.xpath('//tr[contains(@class,"Scontent")]/td[@align]/@href')
	hrefs=selector.xpath('//tr[contains(@class,"Scontent")]/td[@align]/a/@href')
	# print len(hrefs)
	if len(hrefs)==1:
		newUrl='http://www.ttmeiju.com/'+hrefs[0]
	else:
		newUrl='http://www.ttmeiju.com/'+hrefs[0]
		#other big program
	print newUrl
	seedstr = '\n'.join(analyUrl(newUrl))

	return seedstr


def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        print path+' 创建成功'
        os.makedirs(path)
        return True
    else:
        print path+' 目录已存在'
        return False

def analyUrl(url):
	
	print url	
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//tbody[@id="seedlist"]/tr')
	listStr=[]
	if len(hrefs)>0:
		
		info=hrefs[0].xpath('td/a/@href')
	for href in hrefs:
		info=href.xpath('td/a[contains(@href,"/seed/")]/*')
		global movieName
		if href.xpath('td/a[contains(@href,"/seed/")]/font'):
			movieName=href.xpath('td/a[contains(@href,"/seed/")]/font')[0].text.strip()
		else:
			movieName=str(href.xpath('td/a[contains(@href,"/seed/")]')[0].text).strip()
		# print movieName

		if '720' in movieName:
			# print '720'
			sourceUrl=str(href.xpath('td/a[@target]/@href'))
			sourceName=str(href.xpath('td/a[@target]/@title'))
			namem=href.xpath('td/a[@target]')
			n=0
			downloadStr=''
			
			for detail in namem:
				if '百度' in str(detail.attrib.get('title')):
					# print 'baidu'
					downloadStr=str(detail.attrib.get('title'))+':'+str(detail.attrib.get('href'))+'\n'
					# while n<len(namem):			
					# 	downloadStr=downloadStr+str(namem[n].attrib.get('title'))+':'+str(namem[n].attrib.get('href'))+'\n'
					# 	n=n+1
					size=str(href.xpath('td[4]')[0].text).strip()
					mtype=str(href.xpath('td[5]')[0].text).strip()
					zimu=str(href.xpath('td[6]')[0].text).strip()

					# fo.write(movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr)
					# print movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr
					listStr.append(movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr)

				elif '磁力链' in str(detail.attrib.get('title')):
					# print 'baidu'
					downloadStr=str(detail.attrib.get('title'))+':'+str(detail.attrib.get('href'))+'\n'
					# while n<len(namem):			
					# 	downloadStr=downloadStr+str(namem[n].attrib.get('title'))+':'+str(namem[n].attrib.get('href'))+'\n'
					# 	n=n+1
					size=str(href.xpath('td[4]')[0].text).strip()
					mtype=str(href.xpath('td[5]')[0].text).strip()
					zimu=str(href.xpath('td[6]')[0].text).strip()

					# fo.write(movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr)
					# print movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr
					listStr.append(movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr)
	return listStr

	
def  getUrl(url):
	r = requests.get(url)
	data = r.text
	link_list =re.findall(r"(?<=href=\").+?(?=\")" ,data)
	return link_list

def  geturlList(link_list):
	urlList=[]
	for url in link_list:
	    if '/seed/' in url:
	    	newUrl='http://www.ttmeiju.com/'+url
	    	seedUrl=getUrl(newUrl);
	        for url in seedUrl:
	            if '/meiju/' in url:
	                pass
	                url='http://www.ttmeiju.com/'+url
	                urlList.append(url)
	    if '/meiju/' in url:
	    	newUrl='http://www.ttmeiju.com/'+url
	    	urlList.append(newUrl)
	return urlList
def removeD(list):
	newlist=[]
	for x in list:
		if x not in newlist:
			newlist.append(x)
	return newlist
def gettitle(url):
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//div[@class="hd"]')
	for href in hrefs:
		t=''
		for title in href.text:
			t=t+title
			if title==' ':
				break
		# print t
		return t

searchMovie('夏洛克')

