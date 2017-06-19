# -- coding: UTF-8 -- 
import os
import re
import requests
from lxml import html
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Firefox()
# headers = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Host': 'www.ctfile.com',
#     'Proxy-Connection': 'keep-alive',
#     'Referer':'https://www.ctfile.com/',
#     'Cookie': 'Hm_lvt_74590c71164d9fba556697bee04ad65c=1496372413,1496373199,1496383649,1497857804; ct_uid=e9a0d03f40f9327f008cb2ea02a2d734; unique_id=3c6c03; clicktopay=1496373051617; Hm_lpvt_74590c71164d9fba556697bee04ad65c=1497857833; PHPSESSID=oiao7vdcs8k8r7rms3pl9t5gt3; pubcookie=VzIGNwc1VGhSYFE%2FB2sJPlNcCW8DDQMxXGAEPgBvBGwDZA8%2BADVQYQM%2BU0RXe1QnAioBPQNrUT8NCANtWjJRMVc3BjUHN1RlUmVRMAdTCTpTZQluAzADOVxjBDUAawRsA28PTQB0UCkDKFNnV2VUOwINAW8DMFFrDTYDOVo0UTdXOwY3BzNUVVI0UWMHaQlqU2cJYwM8AzBcYAQ2AD0ENgNuD2gANlBqAz5TMldvVG8CYQE4AzVRNw1jA2daN1FkV2AGNgdkVGg%3D',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
Cookie='Hm_lvt_74590c71164d9fba556697bee04ad65c=1496372413,1496373199,1496383649,1497857804; ct_uid=e9a0d03f40f9327f008cb2ea02a2d734; unique_id=3c6c03; clicktopay=1496373051617; Hm_lpvt_74590c71164d9fba556697bee04ad65c=1497857833; PHPSESSID=oiao7vdcs8k8r7rms3pl9t5gt3; pubcookie=VzIGNwc1VGhSYFE%2FB2sJPlNcCW8DDQMxXGAEPgBvBGwDZA8%2BADVQYQM%2BU0RXe1QnAioBPQNrUT8NCANtWjJRMVc3BjUHN1RlUmVRMAdTCTpTZQluAzADOVxjBDUAawRsA28PTQB0UCkDKFNnV2VUOwINAW8DMFFrDTYDOVo0UTdXOwY3BzNUVVI0UWMHaQlqU2cJYwM8AzBcYAQ2AD0ENgNuD2gANlBqAz5TMldvVG8CYQE4AzVRNw1jA2daN1FkV2AGNgdkVGg%3D'
cookies=[] 
for line in Cookie.split(';'):  
  key,value=line.split('=',1)#1代表只分一次，得到两个数据  
  # cookies[key]=value 
  small={} 
  small['name']=key
  small['value']=value
  cookies.append(small) 
print cookies

# driver.delete_all_cookies()
# cookie= driver.get_cookies()

for x in cookies:
	print x
	driver.add_cookie(x)
# time.sleep(12) 

driver.get("https://home.ctfile.com/#item-files")

time.sleep(12) 

response=driver.page_source
selector = html.fromstring(response)
# hrefs=selector.xpath('//div[@class="video-cell clearfix"]')
# print len(hrefs)


