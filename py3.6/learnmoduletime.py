#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

#http://www.cnblogs.com/tkqasn/p/6001134.html
#https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime
#https://docs.python.org/3/library/time.html?highlight=time#module-time
#有空详细看下doc...
#time 模块

'''
time模块中时间表现的格式主要有三种：
a、timestamp时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量time.time()
b、struct_time时间元组，共有九个元素组。time.localtime()
c、format time 格式化时间，已格式化的结构使时间更具可读性。包括自定义格式和固定格式。

格式转换：
strct_time-->format string  strftime 反之 strptime
strut_time-->timestamp  mktime 反之localtime,gmtime

strut_time-->%a%b%d%H:%M%:%S %Y串 asctime
Timestamp-->%a%b%d%H:%M%:%S %Y串  ctime

struct_time元组元素结构
属性                            值
tm_year（年）                  比如2011 
tm_mon（月）                   1 - 12
tm_mday（日）                  1 - 31
tm_hour（时）                  0 - 23
tm_min（分）                   0 - 59
tm_sec（秒）                   0 - 61
tm_wday（weekday）             0 - 6（0表示周日）
tm_yday（一年中的第几天）        1 - 366
tm_isdst（是否是夏令时）        默认为-1

format time结构化表示

格式	含义
%a	本地（locale）简化星期名称
%A	本地完整星期名称
%b	本地简化月份名称
%B	本地完整月份名称
%c	本地相应的日期和时间表示
%d	一个月中的第几天（01 - 31）
%H	一天中的第几个小时（24小时制，00 - 23）
%I	第几个小时（12小时制，01 - 12）
%j	一年中的第几天（001 - 366）
%m	月份（01 - 12）
%M	分钟数（00 - 59）
%p	本地am或者pm的相应符
%S	秒（01 - 61）
%U	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。
%w	一个星期中的第几天（0 - 6，0是星期天）
%W	和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x	本地相应日期
%X	本地相应时间
%y	去掉世纪的年份（00 - 99）
%Y	完整的年份
%Z	时区的名字（如果不存在为空字符）
%%	‘%’字符

'''

#主要time生成方法和time格式转换方法实例

print(time.time())  #1496284159.9776962

#struct_time to timestamp
print(time.mktime(time.localtime())) #1496284160.0

#生成struct_time
# timestamp to struct_time 本地时间
print(time.localtime())  #time.struct_time(tm_year=2017, tm_mon=6, tm_mday=1, tm_hour=10, tm_min=29, tm_sec=20, tm_wday=3, tm_yday=152, tm_isdst=0)
print(time.localtime(time.time())) #time.struct_time(tm_year=2017, tm_mon=6, tm_mday=1, tm_hour=10, tm_min=29, tm_sec=20, tm_wday=3, tm_yday=152, tm_isdst=0)

# timestamp to struct_time 格林威治时间utc时区
print(time.gmtime())  #time.struct_time(tm_year=2017, tm_mon=6, tm_mday=1, tm_hour=2, tm_min=29, tm_sec=20, tm_wday=3, tm_yday=152, tm_isdst=0)
print(time.gmtime(time.time())) #time.struct_time(tm_year=2017, tm_mon=6, tm_mday=1, tm_hour=2, tm_min=29, tm_sec=20, tm_wday=3, tm_yday=152, tm_isdst=0)

#format_time to struct_time
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')) #time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1)

#生成format_time
#struct_time to format_time
print(time.strftime("%Y-%m-%d %X")) #2017-06-01 10:29:20
print(time.strftime("%Y-%m-%d %X",time.localtime()))  #2017-06-01 10:29:20

#生成固定格式的时间表示格式
print(time.asctime(time.localtime())) #Thu Jun  1 10:29:20 2017
print(time.ctime(time.time()))   #Thu Jun  1 10:29:20 2017

#time.sleep(secs)：线程推迟指定的时间运行。单位为秒
#time.clock()在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
time.sleep(1)  
print ("clock1:%s" % time.clock()) 
time.sleep(1)  
print ("clock2:%s" % time.clock()) 
time.sleep(1)  
print ("clock3:%s" % time.clock())
#其中第一个clock()输出的是程序运行时间第二、三个clock()输出的都是与第一个clock的时间间隔


#time加减
#timestamp加减单位以秒为单位
t1=time.time()
t2=t1+10

print (time.ctime(t1))  #Thu Jun  1 11:00:49 2017
print (time.ctime(t2))  #Thu Jun  1 11:00:59 2017


#datetime模块

#datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。
import datetime

#1.返回当前时间
print(datetime.datetime.now()) #2017-06-01 13:29:27.664655

#2.时间戳转换成日期
print(datetime.date.fromtimestamp(1178766678)) #2007-05-10
#datetime.date(2007, 5, 10)

#3.当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(+3)) #2017-06-04 13:29:27.695657
#datetime.datetime(2017, 5, 12, 17, 12, 42, 124379)

#4.当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #2017-05-29 13:29:27.707658
#datetime.datetime(2017, 5, 6, 17, 13, 18, 474406)

#5.当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(hours=3))#2017-06-01 16:29:27.715658
#datetime.datetime(2017, 5, 9, 20, 13, 55, 678310)

#6.当前时间+30分钟
print(datetime.datetime.now() + datetime.timedelta(minutes=30))#2017-06-01 13:59:27.723658
#datetime.datetime(2017, 5, 9, 17, 44, 40, 392370)

#等等等等

