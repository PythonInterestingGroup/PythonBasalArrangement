# -*- coding: utf-8 -*-
#author dm

#Cookie
# Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密)。
#http.cookiejar功能强大，我们可以利用本模块的CookieJar类的对象来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
#它们的关系： CookieJar–派生– > FileCookieJar–派生– > MozillaCookieJar和LWPCookieJar
#工作原理：创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。查看登录之后才能看到的信息。

'''
from urllib import request
from http import cookiejar

#将Cookie保存到变量中
if __name__=='__main__':
    cookie=cookiejar.CookieJar()  #声明一个cookie对象实例
    handler=request.HTTPCookieProcessor(cookie) #创建cookie处理器，即cookiehandler
    opener=request.build_opener(handler) #创建opener
    response=opener.open('http://www.baidu.com')
    for item in cookie:  #打印cookie信
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)

#保存Cookie到文件
if __name__=='__main__':
    filename='cookie.txt'
    cookie=cookiejar.MozillaCookieJar(filename)
    handler=request.HTTPCookieProcessor(cookie)
    opener=request.build_opener(handler)
    response1=opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)
#ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
#ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入。

#从文件中获取cookie并访问
if __name__=='__main__':
    filename='cookie.txt'
    cookie=cookiejar.MozillaCookieJar()
    cookie.load(filename,ignore_discard=True,ignore_expires=True)  # #从文件中读取cookie内容到变量
    handler=request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response=opener.open('http://www.baidu.com')
    #print(response.read().decode('utf-8'))
'''
#模拟登陆伯乐在线,获取相亲MM的联系方式
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
import  json
if __name__=="__main__":
    login_url = 'http://date.jobbole.com/wp-admin/admin-ajax.php'
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






