# -- coding: UTF-8 -- 
import os
import re
import requests
from lxml import html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
Cookie='Hm_lvt_74590c71164d9fba556697bee04ad65c=1496372413,1496373199,1496383649,1497857804; ct_uid=e9a0d03f40f9327f008cb2ea02a2d734; unique_id=3c6c03; clicktopay=1496373051617; Hm_lpvt_74590c71164d9fba556697bee04ad65c=1497857833; PHPSESSID=oiao7vdcs8k8r7rms3pl9t5gt3; pubcookie=VzIGNwc1VGhSYFE%2FB2sJPlNcCW8DDQMxXGAEPgBvBGwDZA8%2BADVQYQM%2BU0RXe1QnAioBPQNrUT8NCANtWjJRMVc3BjUHN1RlUmVRMAdTCTpTZQluAzADOVxjBDUAawRsA28PTQB0UCkDKFNnV2VUOwINAW8DMFFrDTYDOVo0UTdXOwY3BzNUVVI0UWMHaQlqU2cJYwM8AzBcYAQ2AD0ENgNuD2gANlBqAz5TMldvVG8CYQE4AzVRNw1jA2daN1FkV2AGNgdkVGg%3D'
print type(Cookie)
a=Cookie.split(';')
print a
cookies={}  
for line in Cookie.split(';'):  
  key,value=line.split('=',1)#1代表只分一次，得到两个数据  
  cookies[key]=value 
print cookies

# print type(a)
# b=''.join(a)
# print type(b)
# cookies={}  
# for x in a:
# 	print x
# 	key,value=x.split('=',1)#1代表只分一次，得到两个数据  
# 	cookies[key]=value 
# print cookies
# # for line in Cookie.split(';'):  
# #   key,value=line.split('=',1)#1代表只分一次，得到两个数据  
# #   cookies[key]=value 
# # print cookies
# lista='a=1;b=2;c=3'
# print type(lista)