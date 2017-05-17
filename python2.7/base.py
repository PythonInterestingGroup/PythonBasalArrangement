#!/usr/bin/Python
#-*- coding: utf-8 -*-
import sys,os
#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     print os.getcwd()
     print os.path.abspath(sys.argv[0])
     path = sys.path[0]
     print path
     print os.path.dirname(path)
     print  os.path.split(os.path.realpath(__file__))[0]

     # path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         print 1
         return path
     elif os.path.isfile(path):
         print 2
         return os.path.dirname(path)
#打印结果
# print cur_file_dir()

# if getattr(sys, 'frozen', False):
#     application_path = os.path.dirname(sys.executable)
# elif __file__:
#     application_path = os.path.dirname(__file__)

# config_path = os.path.join(application_path, config_name)

print sys.path[0]
print sys.argv[0]
print os.chdir(sys.path[0])
print sys.executable
# 获取脚本运行目录
print os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
print os.getcwd()  
