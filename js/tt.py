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

browser = webdriver.Firefox()
browser.get('http://www.baidu.com/')