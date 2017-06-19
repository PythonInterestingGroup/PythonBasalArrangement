# -- coding: UTF-8 -- 
import os
import re
import requests
from lxml import html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome()
driver.get("http://www.acfun.cn/search/?#query=韩服王者")
# assert "Python" in driver.title
# elem = driver.find_element_by_id("search-text")
# q='韩服王者'
# elem.send_keys(q.decode())
# # elem.send_keys(q)
# elem.send_keys(Keys.RETURN)
# print (driver.page_source)

# url='http://www.btans.com/search/%s-first-asc-1'%name
# print url	
response=driver.page_source
selector = html.fromstring(response)
hrefs=selector.xpath('//div[@class="video-cell clearfix"]')
print len(hrefs)

sourcelist=[]
# if len(hrefs)>0:
# 	href=hrefs[0]
# 	name=href.xpath('div[@class="item-title"]/a/span')
# 	sourcelist.append(name[0].text)
# 	downUrl=href.xpath('div[@class="item-bar"]/a/@href')
# 	# print len(downUrl)
# 	for x in downUrl:
# 		sourcelist.append(x)
# return sourcelist
