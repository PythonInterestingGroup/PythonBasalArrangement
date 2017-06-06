#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python
# create_table_sql = "CREATE TABLE chat_logs(group_number VARCHAR(255) UNIQUE PRIMARY KEY,group_name VARCHAR(255) UNIQUE ,qq VARCHAR(255) NOT NULL,nickname VARCHAR(255) UNIQUE,mark VARCHAR(255) UNIQUE,content VARCHAR(255) UNIQUE,create_time VARCHAR(255) UNIQUE)"
# cursor.execute(create_table_sql)

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='123456', database='test')

cursor = conn.cursor()
# 创建user表:
cursor.execute("SET NAMES utf8")

cursor.execute('create table chat_logs (group_number varchar(20) primary key, group_name varchar(20),qq varchar(20),nickname varchar(20),mark varchar(20),content varchar(20),create_time varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('insert into user (id, name) values (%s, %s)', ('1', 'Michael'))
# print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))
# values = cursor.fetchall()
# print(values)
# 关闭Cursor和Connection:
# cursor.close()
# conn.close()