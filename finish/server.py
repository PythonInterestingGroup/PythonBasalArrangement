#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# server.py
 
#包含wsgiref模块，主要用于httpserver
from wsgiref.simple_server import make_server
 
#包含刚刚自己写的api1模块
from api import application
 
#开启服务器，参数是IP，端口，和刚刚定义的api函数名
httpd = make_server('192.168.63.211', 8001, application)
 
#连接成功输出
print "Serving HTTP on port 8001..."
 
#记录并且打印请求日志
httpd.serve_forever()