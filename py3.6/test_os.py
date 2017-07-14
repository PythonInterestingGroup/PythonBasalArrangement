# -*- coding: utf-8 -*-
#author dm

#练习
#1.利用os模块编写一个能实现dir -l输出的程序。
#打印当前目录所有文件，大小，时间，名称
from datetime import datetime
import os

pwd = os.path.abspath('.')
#pwd = os.path.abspath('')  ##返回绝对路径 D:\dmtest\PythonBasalArrangement\py3.6
print(pwd)
print('      Size     Last Modified  Name')
print('------------------------------------------------------------')
#for f in os.listdir(os.getcwd()):#获得当前目录下的内容
print(os.listdir(pwd))
for f in os.listdir(pwd):   #获取指定目录下的内容
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '\\' if os.path.isdir(f) else ''
    #flag = '\\' if os.path.isdir(pwd + '\\' + f) else ''
    #flag='\\' if os.path.isdir(os.path.join(pwd,f)) else ''
    '''
    if(os.path.isdir(os.path.join(pwd,f))):
        flag=('\\')
    else:
        flag=('')
    '''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

#2.编写一程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

def searchf(path,keyword):
    for f in os.listdir(path):
        f1=os.path.join(path,f)
        if os.path.isdir(f1):
            searchf(f1,keyword)
        else:
            os.path.isfile(f1)
            if keyword in f1:
                print(f1)
path=os.getcwd()  #当前路径
print(path)
searchf(path,'task')
