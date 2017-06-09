# coding:utf-8
import pymysql
import json
import random
from qqbot import QQBotSlot as qqbotslot, RunBot
import requests
import searchm
import fh
KEY='70a315f07d324b3ea02cf21d13796605'
def answerQ(question):
    apiUrl='http://www.tuling123.com/openapi/api'
    # print apiUrl
    data={'key':KEY,'info':question,'userid':'qq'}
    # try:
    payload = {'key':KEY,'info':question}
    try:
		r=requests.post(apiUrl,data=payload)
		mytext = json.loads(r.text)
		return mytext['text']
    except Exception as e:
    	# print e
		return '我不知道,不会百度么'
    # return result
 #    try:
 #    	r = requests.post(apiUrl, data=payload)
 #    	text = json.loads(r.text)
 #    	print text
	# except Exception as e:
 #    	print '超时'


def selectChatContent(content_type):
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
	# now = datetime.datetime.now()
	# createtime=now.strftime('%Y-%m-%d %H:%M:%S')  
	# 查询数据  
	try:
		sql = "SELECT * from duanzi"
		cursor.execute(sql)  
		result = cursor.fetchall()
		# print result
		connect.commit()
		# print('select success', cursor.rowcount, ' record')
	except Exception as e:
		raise
	finally:
	    connect.close();
	    return result
def getdzList():
	dzList=selectChatContent('1')
	# newList=sorted(dzList,key=lambda x:int(x[2]),reverse = True)
	newList=sorted(dzList,key=lambda x:int(x[2]))
	# bestDZ=newList[0][3]
	# return bestDZ
	# print len(newList)
	mylist=[]
	for duanzi in newList:
		# print duanzi[3]
		mylist.append(duanzi[3])
	return mylist
def getrandom():
	thelist= getdzList()
	t=random.randint(0, len(thelist))
	print t
	return thelist[t]

@qqbotslot
def onQQMessage(bot, contact, member, content):
    # if '@ME' in content:
	if '段子' in content:
	    bot.SendTo(contact, '%s'%getrandom())
	elif 'fh ' in content:
		detail=content.replace('fh ','')
		if fh.searchFH(detail):
			bot.SendTo(contact, fh.searchFH(detail))
		else:
			bot.SendTo(contact, '资源18x,请联系群主')
	elif '黄图' in content:
	    bot.SendTo(contact, '请联系群主')
	elif '美剧 ' in content:
	    # bot.SendTo(contact, '搜索中,请稍候...')
	    detail=content.replace('美剧 ','')
	    # seedList=searchm.searchMovie(detail)
	    if searchm.searchMovie(detail):
	    	bot.SendTo(contact, searchm.searchMovie(detail))
	    else:
	    	bot.SendTo(contact, '未搜索到相关资源')


	    # for x in seedList:
	    # 	bot.SendTo(contact, '%s'%x)

   	elif '@ME' in content:
		bot.SendTo(contact, answerQ(content))
	elif content == '-stop':
		bot.SendTo(contact, 'QQ机器人已关闭')
		bot.Stop()

if __name__ == '__main__':
    # 注意： 这一行之前的代码会被执行两边
    # 进入 RunBot() 后，会重启一次程序（ subprocess.call(sys.argv + [...]) ）
    RunBot()
    # 注意: 这一行之后的代码永远都不会被执行。
    # print answerQ('北京天气')