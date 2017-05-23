# coding:utf-8
import requests
from lxml import html
from lxml import etree
import os
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

# url http://www.ttmeiju.com/meiju/Prison.Break.html
def analyUrl():
	url="http://www.ttmeiju.com/meiju/Prison.Break.html"
	response=requests.get(url).content
	# print response
	selector = html.fromstring(response)
	hrefs=selector.xpath('//tbody[@id="seedlist"]/tr')
	# print hrefs
	# print len(hrefs)
	info=hrefs[0].xpath('td/a/@href')
	# print info
	# print len(info)
	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  

	fo=open('%s/meiju.txt'%(path),'w')

	for href in hrefs:
		info=href.xpath('td/a[contains(@href,"/seed/")]/*')
		global movieName
		if href.xpath('td/a[contains(@href,"/seed/")]/font'):
			# print href.xpath('td/a[contains(@href,"/seed/")]/font')
			movieName=href.xpath('td/a[contains(@href,"/seed/")]/font')[0].text.strip()
			# print href.xpath('td/a[contains(@href,"/seed/")]/font')[0].text
		else:
			movieName=str(href.xpath('td/a[contains(@href,"/seed/")]')[0].text).strip()
		# print movieName
		sourceUrl=str(href.xpath('td/a[@target]/@href'))
		sourceName=str(href.xpath('td/a[@target]/@title'))
		# print sourceName
		namem=href.xpath('td/a[@target]')
		print len(namem)
		print namem[0].attrib.get('title')
		n=0
		downloadStr=''
		while n<len(namem):
						
		# downloadStr=namem[0].attrib.get('title')+namem[0].attrib.get('href')+'\n'+namem[1].attrib.get('title')+namem[1].attrib.get('href')+'\n'+namem[2].attrib.get('title')+':'+namem[2].attrib.get('href')+'\n'
			
			downloadStr=downloadStr+str(namem[n].attrib.get('title'))+':'+str(namem[n].attrib.get('href'))+'\n'
			# print downloadStr
			n=n+1
		print downloadStr
		size=str(href.xpath('td[4]')[0].text).strip()
		mtype=str(href.xpath('td[5]')[0].text).strip()
		zimu=str(href.xpath('td[6]')[0].text).strip()

		fo.write(movieName+':'+'_'+size+'_'+mtype+'_'+zimu+'_'+':'+'\n'+downloadStr)
	fo.close()


if __name__ == '__main__':
	analyUrl()

