# coding:utf-8

import datetime
import time 
import requests
import json
import sys
import os
def getDateUnix():
	return time.mktime(datetime.datetime.now().timetuple())
def getUrl():
	return 'http://iu.snssdk.com/neihan/stream/mix/v1/?tag=joke&os_version=10.1.1&os_api=18&app_name=joke_essay&channel=App%%20Store&device_platform=iphone&live_sdk_version=174&&openudid=25adf6c3bb1f51523606523f4252e49e3c619921&device_type=iPhone9,1&version_code=6.3.1&ac=WIFI&screen_width=750&aid=7&content_type=-102&count=30&double_col_mode=0&essence=1message_cursor=175514038&min_time=%s&mpic=1'%(getDateUnix())
print getUrl()	
def getContent():
	while True:
		try:
			url=getUrl()
			print url
			response=requests.get(url).content
			jsonData = json.loads(response)
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
								print joker['group']['text']
							# bury_count 踩 comment_count 评论 share_count 转发 
							# share_url for 101
			# time.sleep(30)
		except Exception as e:
			raise
getContent()