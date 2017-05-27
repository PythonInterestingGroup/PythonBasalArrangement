# coding:utf-8
import requests
from lxml import html
import os
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

def analyUrl():
	url="http://www.ttmeiju.com/meiju/Prison.Break.html"
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//tbody[@id="seedlist"]/tr')
	info=hrefs[0].xpath('td/a/@href')
	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  

	fo=open('%s/meiju.txt'%(path),'w')

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
		print downloadStr
		size=str(href.xpath('td[4]')[0].text).strip()
		mtype=str(href.xpath('td[5]')[0].text).strip()
		zimu=str(href.xpath('td[6]')[0].text).strip()

		fo.write(movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr)
	fo.close()


if __name__ == '__main__':
	analyUrl()

