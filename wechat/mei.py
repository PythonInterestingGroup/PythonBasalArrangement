# -*- coding: utf-8 -*-
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
import  json
login_url = 'http://www.jobbole.com/wp-admin/admin-ajax.php'
user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
head={'User-Agnet': user_agent, 'Connection': 'keep-alive'}
Login_Data = {}  #form_data
Login_Data['action'] = 'user_login'
Login_Data['redirect_url'] = 'http://data.jobbole.com/'
Login_Data['remember_me'] = '1'  # 是否一个月内自动登陆
Login_Data['user_login'] = 'diamondm'  # 改成你自己的用户名
Login_Data['user_pass'] = '@H)RUnq42PdD2bt*'  # 改成你自己的密码
logingpostdata = parse.urlencode(Login_Data).encode('utf-8')  #使用urlencode方法转换标准格式
cookie = cookiejar.CookieJar()
cookie_support = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(cookie_support)
req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

date_url = 'http://date.jobbole.com/wp-admin/admin-ajax.php'
Date_Data = {}
Date_Data['action'] = 'get_date_contact'
Date_Data['postId'] = '4406'
datepostdata = parse.urlencode(Date_Data).encode('utf-8')
req2 = request.Request(url=date_url, data=datepostdata, headers=head)
try:
    response1 = opener.open(req1)
    response2 = opener.open(req2)
    html = response2.read().decode('utf-8')
    results = json.loads(html)
    print(results)
    index = html.find('jb_contact_email')
    print('联系邮箱:%s' % html[index + 19:-2])

except error.URLError as e:
    if hasattr(e, 'code'):
        print("HTTPError:%d" % e.code)
    elif hasattr(e, 'reason'):
        print("URLError:%s" % e.reason)