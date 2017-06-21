#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

import sys

print(sys.getdefaultencoding())

if __name__ == '__main__':
	response = request.urlopen("https://www.baidu.com")
	html = response.read()
	html = html.decode('utf-8')
	print(html)
