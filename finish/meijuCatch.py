# coding:utf-8
import os
import sys
import re
import requests
from lxml import html
reload(sys)
sys.setdefaultencoding('utf8')
def analyUrl(url):
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//tbody[@id="seedlist"]/tr')
	if len(hrefs)>0:
		
		info=hrefs[0].xpath('td/a/@href')
	for href in hrefs:
		info=href.xpath('td/a[contains(@href,"/seed/")]/*')
		global movieName
		if href.xpath('td/a[contains(@href,"/seed/")]/font'):
			movieName=href.xpath('td/a[contains(@href,"/seed/")]/font')[0].text.strip()
		else:
			movieName=str(href.xpath('td/a[contains(@href,"/seed/")]')[0].text).strip()
		sourceUrl=str(href.xpath('td/a[@target]/@href'))
		sourceName=str(href.xpath('td/a[@target]/@title'))
		namem=href.xpath('td/a[@target]')
		n=0
		downloadStr=''
		while n<len(namem):			
			downloadStr=downloadStr+str(namem[n].attrib.get('title'))+':'+str(namem[n].attrib.get('href'))+'\n'
			n=n+1
		size=str(href.xpath('td[4]')[0].text).strip()
		mtype=str(href.xpath('td[5]')[0].text).strip()
		zimu=str(href.xpath('td[6]')[0].text).strip()

		fo.write(movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr)

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

if __name__ == '__main__':
	baselist=getUrl('http://www.ttmeiju.com/')
	print baselist
	downloadList=geturlList(baselist)
	downloadList=removeD(downloadList)
	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
	fo=open('%s/meiju.txt'%(path),'w')
	for x in downloadList:
		print x
		analyUrl(x)
	fo.close()


