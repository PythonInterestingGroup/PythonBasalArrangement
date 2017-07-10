#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

import chardet

import sys

# print(sys.getdefaultencoding())

if __name__ == '__main__':
	'''
	response = request.urlopen("https://fanyi.youdao.com/")
	html = response.read()
	chardet = chardet.detect(html)
	print(chardet)
	'''
	req = request.Request("http://fanyi.youdao.com/")
	response = request.urlopen(req)
	html = response.read() # geturl() , info() , getcode()
	print("url:",response.geturl())
	print("元信息:",response.info())
	print("statusCode = ",response.getcode())
	html = html.decode("utf-8")
	#print(html)


