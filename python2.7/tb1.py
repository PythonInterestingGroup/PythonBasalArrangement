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
	# res = requests.get("http://pub.alimama.com/items/search.json?q=%s&_t=1491446745748&auctionTag=&perPageSize=40&shopTag=yxjh&t=1491446745809&_tb_token_=gGzz1isBBxVq&pvid=10_202.96.204.154_871_1491446230711"%name)
	# res = requests.get("http://pub.alimama.com/promo/search/index.htm?q=男装&_t=1491449422417&toPage=1&perPageSize=40")
	# print res.text
	# save('1.json',res.text)

	# res2 = requests.get("http://pub.alimama.com/promo/search/index.htm?q=男装&_t=1491449422417&toPage=1&perPageSize=40")
	# res2 = requests.get("http://pub.alimama.com/items/search.json?q=%s&_t=1491449422417&toPage=2&perPageSize=40&auctionTag=&shopTag=yxjh&t=1491451368679&_tb_token_=gGzz1isBBxVq&pvid=10_202.96.204.154_567_1491449989952"%name)
	# res2 = requests.get("http://pub.alimama.com/items/search.json?q=%s&_t=1491446745748&toPage=2&perPageSize=40&auctionTag=&shopTag=yxjh&t=1491446745809&_tb_token_=gGzz1isBBxVq&pvid=10_202.96.204.154_567_1491449989952"%name)
	
	res2 = requests.get("http://pub.alimama.com/common/code/getAuctionCode.json?auctionid=528114332523&adzoneid=76790852&siteid=23150503&scenes=1&t=1491466158623&_tb_token_=gGzz1isBBxVq&pvid=10_202.96.204.154_725_1491466132743")
	print res2.text
	save('2.json',res2.text)


getgoods('男装')