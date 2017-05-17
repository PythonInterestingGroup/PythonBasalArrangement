# -*- coding: utf-8 -*-

# api.py
#包含了处理URL的模块
import urlparse
#包含了处理json的模块
import json
#包含了处理字符串和字典的模块
from cgi import parse_qs, escape
 
#定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
#定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'text/html')])
    #environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    #return '{data = %s}' % (environ)
    #return urlparse.parse_qs(environ['QUERY_STRING'])
    #获取当前get请求的所有数据，返回是string类型
    params = parse_qs(environ['QUERY_STRING'])
    #获取get中key为name的值
    name = params.get('name', [''])[0]
    #以此类推
    website = params.get('website', [''])[0]
 
    user = params.get('user', [''])[0]
 
    password = params.get('pass',[''])[0]
    #组成一个数组，数组中只有一个字典
    dic = [{'name':name,'website':website,'user':user,'password':password}]
    #生成一个大字典
    data = {'data':dic}
    #然后返回
    return json.dumps(data)