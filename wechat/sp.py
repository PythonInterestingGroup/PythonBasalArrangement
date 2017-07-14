# coding:utf-8

import datetime
import time 
import requests
import json
import sys
import os
import pymysql
import urllib  

def insertChatContent(create_time,content_type,content):
	# 连接数据库  
	connect = pymysql.Connect(  
		host='127.0.0.1',
		port=3306,  
		user='root',  
		passwd='31415926',  
		db='neihan',  
		charset='utf8'  
	)  
	  
	# 获取游标  
	cursor = connect.cursor()  
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 插入数据  
	sql = "INSERT INTO duanzi (create_time,content_type,content) VALUES ( '%s', '%s', '%s')"  

	savecontent = pymysql.escape_string(content)
	data = (createtime,content_type,savecontent)  
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert success', cursor.rowcount, ' record')


def getDateUnix():
	return time.mktime(datetime.datetime.now().timetuple())
def getUrl():

	# return 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%%20Store&device_platform=iphone&live_sdk_version=174&&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&aid=7&content_type=-101&count=30&double_col_mode=0&essence=1message_cursor=175514038&min_time=%s&mpic=1'%(getDateUnix())
	return 'http://lf.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=11219647659&os_version=10.1.1&os_api=18&live_sdk_version=220&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&device_platform=iphone&app_name=joke_essay&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&device_id=30277977392&ac=WIFI&screen_width=750&aid=7&version_code=6.4.0&content_type=-101&count=30&double_col_mode=0&essence=1&latitude=31.19056212218067&longitude=121.4342727649137&message_cursor=175514038&min_time=%s&mpic=1&video_cdn_first=1'%(getDateUnix())
print getUrl()	
def getContent():
	while True:
		try:
			url=getUrl()
			# print url
			response=requests.get(url).content
			# print response
			jsonData = json.loads(response)
			# print jsonData
			if jsonData['message']=='success':
				if len(jsonData['data']['tip'])>5:
					dataArr=jsonData['data']['data']
					# print len(dataArr)
					for joker in dataArr:
						# if joker.has_key('group'):
						if 'group' in joker.keys():
							# print joker['group']['digg_count']
							# print joker['group']['text']
							# print joker['group']['create_time']
							if joker['group']['digg_count']>10000:
								# insertChatContent(joker['group']['create_time'],joker['group']['digg_count'],joker['group']['text'])
								# print joker['group'].keys()
								print joker['group']['origin_video']['url_list'][0]['url']
								# urllib.urlretrieve(joker['group']['origin_video'],"1.mp4")  

							# bury_count 踩 comment_count 评论 share_count 转发 
							# share_url for 101
			time.sleep(30)
		except Exception as e:
			raise
getContent()