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
	selector = html.fromstring(response)
	hrefs=selector.xpath('//tbody[@id="seedlist"]/tr/td/a/@href')
	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
	for x in hrefs:
		print x+'/n'



if __name__ == '__main__':
	analyUrl()