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
    # hrefs = selector.xpath('//div/table[@class="latesttable"]')
    # hrefs=selector.xpath('//div')
	# hrefs = selector.xpath(u'//tbody[id="seedlist"]/td/@href')
	# hrefs=selector.xpath('//tr[@class="Scontent1"]/td/a/@href')
	# hrefs=selector.xpath('//tbody[@id="seedlist"]/tr/td/a[contains(@href,"/seed/")]')
	hrefs=selector.xpath('//tbody[@id="seedlist"]/tr/td/a')
	#normalize-space 空格
	# hrefs2=selector.xpath('//tbody[@id="seedlist"]/tr/td/a/@href')
	# print '123'+hrefs2[0]
	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
	fo=open('%s/meiju.txt'%(path),'w')
	# fo.write(hrefs[1].xpath('@href'))
	# font=hrefs[0].xpath['/font']
	# info = hrefs[0].xpath('string(.)') 
	# print '11'+font.text
	for href in hrefs:
		# print href.xpath('@href')
		# print href.text
		# print href
		# name=href.xpath('a[contains(@href,"/seed/")]/@href')
		# print href.attrib.get('href')
		# print href
		if 'seed' in href.attrib.get('href'):
			# print href.attrib.get('href')
			if '越狱' in href.text:
				# print href.text
				# print 'have'
				fo.write(href.text.strip()+':'+'\n')
				# fo.write(str(href.attrib.get('title')+href.text).strip()+'\n')


			else:
				# print 'font'
				info = href.xpath('string(.)') 
				print info
				# font=href.xpath('/font')
				# # print href.xpath('/font')
				# print font.text
				fo.write(info.strip()+':'+'\n')
				# fo.write(str(href.attrib.get('title')+info).strip()+'\n')
			# fo.write(str(href.attrib.get('href')+href.text).strip()+'\n')
		else:
			
		# print name
		# print name
		# if name.text:
		# 	print name
			# print name.attrib.get('href')
			# fo.write(href.text+':'+'\n')
			# fo.write(name.text)

		# print href.attrib.get("title")
		# print href.attrib.get("href")
		# print href.xpath('@title')
		# fo.write(href.attrib.get("title")+':'+href.attrib.get("href")+'\n')
		# fo.write(str(href.attrib.get("title"))+':'+str(href.attrib.get("href"))+'\n')
		# print json.dumps(href.xpath('@title'))
		# u=json.dumps(href.xpath('@title'))
		# e=u.decode("unicode-escape")
		# print e

		# detailHref=href.xpath('@href');
		# print detailHref
		# print href
		# fo.write(href.xpath(href.xpath('@href')+'\n')
		# fo.write(e+':'+json.dumps(href.xpath('@href'))+'\n')
		# fo.write(e+':'+json.dumps(href.xpath('@href'))+'\n')

		# print href
		# json=href.text
		# print json
	# fo.close()

	fo.close()


if __name__ == '__main__':
	analyUrl()