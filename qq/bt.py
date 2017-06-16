# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
from lxml import html
reload(sys)
sys.setdefaultencoding('utf8')
# http://www.btans.com/search/%E9%95%BF%E5%9F%8E-first-asc-1
def changeUrl(name):
	url='http://www.btmeet.org/search/%s.html'%name
	print url
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//div[@class="search-item"]/div/h3')
	# print hrefs
	for href in hrefs:
		# newurl=href.xpath('a/@href')
		# movieName=href.xpath('a/script/@text')
		# print movieName

		# if href:
		newurl=href.xpath('a/@href')[0]
		analyUrl('http://www.btmeet.org/%s'%newurl)
		# else:
		# 	return

def analyUrl(url):
	# print url	
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//div[@class="panel-body"]/a/@href')
	print hrefs[0]
	# sourcelist=[]
	# if len(hrefs)>0:
	# 	href=hrefs[0]
	# 	name=href.xpath('div[@class="item-title"]/a/span')
	# 	sourcelist.append(name[0].text)
	# 	downUrl=href.xpath('div[@class="item-bar"]/a/@href')
	# 	# print len(downUrl)
	# 	for x in downUrl:
	# 		sourcelist.append(x)
	# return sourcelist
def searchFH(name):
	seedstr = '\n'.join(analyUrl(name))
	return	seedstr
print changeUrl('长城')