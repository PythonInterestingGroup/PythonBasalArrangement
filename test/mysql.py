# -*- coding: utf-8 -*-
import pymysql  
import datetime
def onQQMessage(bot, contact, member, content):
	if contact.ctype == 'group':
		insertChatContent(bot,contact,member,content)


def insertChatContent(bot,contact,member,content):
	# 连接数据库  
	connect = pymysql.Connect(  
		host='192.168.0.106',  
		port=3306,  
		user='root',  
		passwd='123456',  
		db='test',  
		charset='utf8'  
	)  
	  
	# 获取游标  
	cursor = connect.cursor()  
	now = datetime.datetime.now()
	createtime=now.strftime('%Y-%m-%d %H:%M:%S')  

		# 插入数据  
	# sql = "INSERT INTO chat_logs (group_number,group_name,qq,nickname,mark,content,create_time) VALUES ( '%s', '%s', '%s','%s','%s', '%s', '%s')"  
	# name = pymysql.escape_string(contact.name)
	# nickname = pymysql.escape_string(member.name)
	# mark = pymysql.escape_string(member.name)
	# data = (contact.qq,name,member.qq,nickname,mark,content,createtime)  
	# cursor.execute(sql % data)  
	create_table_sql = "CREATE TABLE chat_logs(group_number VARCHAR(255) UNIQUE PRIMARY KEY,group_name VARCHAR(255) UNIQUE ,qq VARCHAR(255) NOT NULL,nickname VARCHAR(255) UNIQUE,mark VARCHAR(255) UNIQUE,content VARCHAR(255) UNIQUE,create_time VARCHAR(255) UNIQUE)"
	cursor.execute(create_table_sql)
	# connect.commit()  
	print('insert success', cursor.rowcount, ' record') 
	
