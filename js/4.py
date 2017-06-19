# -- coding: UTF-8 -- 
import os
import re
import requests
from lxml import html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url='https://home.ctfile.com/#item-files'
print url	
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Host': 'www.ctfile.com',
    'Proxy-Connection': 'keep-alive',
    'Referer':'https://www.ctfile.com/',
    'Cookie': 'Hm_lvt_74590c71164d9fba556697bee04ad65c=1496372413,1496373199,1496383649,1497857804; ct_uid=e9a0d03f40f9327f008cb2ea02a2d734; unique_id=3c6c03; clicktopay=1496373051617; Hm_lpvt_74590c71164d9fba556697bee04ad65c=1497857833; PHPSESSID=oiao7vdcs8k8r7rms3pl9t5gt3; pubcookie=VzIGNwc1VGhSYFE%2FB2sJPlNcCW8DDQMxXGAEPgBvBGwDZA8%2BADVQYQM%2BU0RXe1QnAioBPQNrUT8NCANtWjJRMVc3BjUHN1RlUmVRMAdTCTpTZQluAzADOVxjBDUAawRsA28PTQB0UCkDKFNnV2VUOwINAW8DMFFrDTYDOVo0UTdXOwY3BzNUVVI0UWMHaQlqU2cJYwM8AzBcYAQ2AD0ENgNuD2gANlBqAz5TMldvVG8CYQE4AzVRNw1jA2daN1FkV2AGNgdkVGg%3D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response=requests.get(url,headers=headers).content
print response
# selector = html.fromstring(response)
# hrefs=selector.xpath('//div[@class="video-cell clearfix"]')
# print hrefs
# sourcelist=[]
# if len(hrefs)>0:
# 	href=hrefs[0]
# 	name=href.xpath('div[@class="item-title"]/a/span')
# 	sourcelist.append(name[0].text)
# 	downUrl=href.xpath('div[@class="item-bar"]/a/@href')
# 	# print len(downUrl)
# 	for x in downUrl:
# 		sourcelist.append(x)
