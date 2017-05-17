#! usr/bin/python
#coding=utf-8 
#获取相关商品
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def save(filename, contents): 
  fh = open(filename, 'w') 
  fh.write(contents) 
  fh.close() 

def getgoods(name):
	res = requests.get("http://pub.alimama.com/items/search.json?q=%s&_t=1491446745748&toPage=2&perPageSize=40&auctionTag=&shopTag=yxjh&t=1491446745809&_tb_token_=gGzz1isBBxVq&pvid=10_202.96.204.154_567_1491449989952"%name)
	# print res.text
	text = json.loads(res.text)
	listArr=text['data']['pageList']
	# print listArr
	for coupon in listArr:
		print coupon['couponAmount']
		if coupon['couponAmount']!=0:
			print coupon['title']
	# save('2.json',res.text)


getgoods('男装')