#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# Scrapy是一个为了爬取网站数据提取结构性数据而编写的应用框架，可以应用于数据挖掘，信息处理或存储历史数据等一些列的程序中
# install: pip3 install scrapy

# cookies: 指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密)
# http.cookiejar
# MozillaCookieJar and WPCookieJar -> FileCookieJar -> CookieJar
# 工作原理：创建一个带有cookie的opener，在访问登录的URL时，将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。查看登录之后才能看到的信息
# 抓包: Fiddler or chrome://net-internals=> https://segmentfault.com/q/1010000000170012
