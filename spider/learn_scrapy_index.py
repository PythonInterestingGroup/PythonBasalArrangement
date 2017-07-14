# -*- coding: utf-8 -*-
#author dm
#http://blog.csdn.net/c406495762/article/details/72858983

#scrapy入门：http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html
# Scrapy Engine(Scrapy核心) 负责数据流在各个组件之间的流。Spiders(爬虫)发出Requests请求，经由Scrapy Engine(Scrapy核心) 交给Scheduler(调度器)，Downloader(下载器)Scheduler(调度器) 获得Requests请求，然后根据Requests请求，从网络下载数据。Downloader(下载器)的Responses响应再传递给Spiders进行分析。根据需求提取出Items，交给Item Pipeline进行下载。Spiders和Item Pipeline是需要用户根据响应的需求进行编写的。除此之外，还有两个中间件，Downloaders Mddlewares和Spider Middlewares，这两个中间件为用户提供方面，通过插入自定义代码扩展Scrapy的功能，例如去重等。
'''
简单流程如下：
创建一个Scrapy项目；
定义提取的Item；
编写爬取网站的 spider 并提取 Item；
编写 Item Pipeline 来存储提取到的Item(即数据)。
'''

#创建项目 命令： scrapy startproject 项目名
