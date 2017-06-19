import requests
from bs4 import BeautifulSoup
s = requests.Session()
r = s.post('http://www.zhihu.com/login',data={'_xsrf':BeautifulSoup(s.get('http://www.zhihu.com/').content).find(type='hidden')['value']