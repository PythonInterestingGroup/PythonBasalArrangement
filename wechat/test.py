# coding:utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
import time

pagenum = BeautifulSoup(str('[<span class="size"><i></i>6页</span>]'), 'lxml')
print(pagenum)
result=pagenum.p.span.string
print(pagenum.p.span.text)