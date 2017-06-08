# coding:utf-8
import pymysql
import json
import random
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

thelist= getdzList()
t=random.randint(0, len(thelist))
print t
print thelist[t]



	