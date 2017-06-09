# http://www.acfun.cn/search/#query=%E9%9F%A9%E6%9C%8D%E7%8E%8B%E8%80%85
# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
import shutil
from lxml import html
reload(sys)
sys.setdefaultencoding('utf8')

def analyUrl(name):
	url='http://www.acfun.cn/search/#query=%s'%name
	print url	
	response=requests.get(url).content
	selector = html.fromstring(response)
	# hrefs=selector.xpath('//div[@class="video-cell clearfix"]')
	hrefs=selector.xpath('//div[@class="video-list-wrap"]')
	sourcelist=[]
	print len(hrefs)
	# if len(hrefs)>0:
	# 	href=hrefs[0]
	# 	print '1'
	# 	name=href.xpath('div[class="video-cell-right fl"]/div[class="title"]/a')
	# 	print name
	# 	sourcelist.append(name[0].text)
	# 	downUrl=href.xpath('div[class="video-cell-right fl"]/div[class="title"]/a')
		# print len(downUrl)
	return sourcelist
def searchFH(name):
	seedstr = '\n'.join(analyUrl(name))
	return	seedstr
print searchFH('韩服王者')
