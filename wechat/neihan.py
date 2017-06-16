# coding:utf-8
# 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=10483316536&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%20Store&device_platform=iphone&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&live_sdk_version=174&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&device_id=30277977392&aid=7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&content_type=-102&count=30&double_col_mode=0&essence=1&latitude=31.08946115076879&longitude=121.5034942973322&message_cursor=175514038&min_time=0&mpic=1'
# 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=10483316536&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%20Store&device_platform=iphone&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&live_sdk_version=174&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&device_id=30277977392&aid=7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&content_type=-101&count=30&double_col_mode=0&essence=1&latitude=31.08946115076879&longitude=121.5034942973322&message_cursor=175514038&min_time=1496879980&mpic=1'
# 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=10483316536&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%20Store&device_platform=iphone&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&live_sdk_version=174&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&device_id=30277977392&aid=7&city=%E4%B8%8A%E6%B5%B7%E5%B8%82&content_type=-103&count=30&double_col_mode=0&essence=1&latitude=31.08946115076879&longitude=121.5034942973322&message_cursor=175514038&min_time=1496887297&mpic=1'
# 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%20Store&device_platform=iphone&live_sdk_version=174&&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&aid=7&content_type=-102&count=30&double_col_mode=0&essence=1message_cursor=175514038&min_time=0&mpic=1'
# 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%20Store&device_platform=iphone&live_sdk_version=174&&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&aid=7&content_type=-102&count=30&double_col_mode=0&essence=1message_cursor=175514038&min_time=0&mpic=1'
# text=102 image 103 video 101
import datetime
import time 
import requests
import json
import sys
import os
import pymysql
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
	# create_time = pymysql.escape_string(create_time)
	# print create_time
	# content_type = pymysql.escape_string(content_type)
	savecontent = pymysql.escape_string(content)
	data = (createtime,content_type,savecontent)  
	cursor.execute(sql % data)  
	connect.commit()  
	print('insert success', cursor.rowcount, ' record')


def getDateUnix():
	return time.mktime(datetime.datetime.now().timetuple())
def getUrl():
	# return 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&iid=10483316536&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%%20Store&device_platform=iphone&idfa=E8131C7D-8AD5-45A0-8E6A-5F97A90CA5A9&live_sdk_version=174&vid=20FC79DA-3103-42B3-A92E-F2D58B8DFD34&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&device_id=30277977392&aid=7&content_type=-102&count=30&double_col_mode=0&essence=1&latitude=31.08946115076879&longitude=121.5034942973322&message_cursor=175514038&min_time=%s&mpic=1'%(getDateUnix())
	return 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%%20Store&device_platform=iphone&live_sdk_version=174&&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&aid=7&content_type=-102&count=30&double_col_mode=0&essence=1message_cursor=175514038&min_time=%s&mpic=1'%(getDateUnix())
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
								insertChatContent(joker['group']['create_time'],joker['group']['digg_count'],joker['group']['text'])
							# bury_count 踩 comment_count 评论 share_count 转发 
							# share_url for 101
			time.sleep(30)
		except Exception as e:
			raise
getContent()