# coding:utf-8
import requests
from lxml import html
from lxml import etree
import os
import sys
import json
url="http://www.ttmeiju.com/meiju/Prison.Break.html"
response=requests.get(url).content
selector = html.fromstring(response)
hrefs=selector.xpath('//tbody[@id="seedlist"]/tr/td/a')