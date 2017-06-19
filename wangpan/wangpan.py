# coding:utf-8
import os
import sys
import re
import requests
from lxml import html
reload(sys)
sys.setdefaultencoding('utf8')

# https://home.ctfile.com/#item-files/action-index/folder_id-20610733
def analyUrl(url):
	headers = {'cookie':cookiestr}  
	url='https://home.ctfile.com/#item-files/action-index/folder_id-20610733'
	response=requests.get(url).content
	selector = html.fromstring(response)
	print response
if __name__ == '__main__':
	analyUrl('1')