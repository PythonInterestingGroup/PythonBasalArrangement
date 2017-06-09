# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
import shutil
from lxml import html
reload(sys)
sys.setdefaultencoding('utf8')
# http://www.btans.com/search/%E9%95%BF%E5%9F%8E-first-asc-1
def analyUrl(name):
	url='http://www.btans.com/search/%s-first-asc-1'%name
	print url	
	response=requests.get(url).content
	selector = html.fromstring(response)
	hrefs=selector.xpath('//div[@class="search-item"]')
	sourcelist=[]
	if len(hrefs)>0:
		href=hrefs[0]
		name=href.xpath('div[@class="item-title"]/a/span')
		sourcelist.append(name[0].text)
		downUrl=href.xpath('div[@class="item-bar"]/a/@href')
		# print len(downUrl)
		for x in downUrl:
			sourcelist.append(x)
	return sourcelist
def searchFH(name):
	seedstr = '\n'.join(analyUrl(name))
	return	seedstr
# print searchFH('长城')
