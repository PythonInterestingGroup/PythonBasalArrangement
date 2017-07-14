# -*- coding: utf-8 -*-
#author dm

import os
print(os.name)  #如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
#print(os.uname())  win不存在
#os模块的某些函数是跟操作系统相关的。

#环境变量保存在os.environ这个变量
print(os.environ)

#要获取某个环境变量的值，可以调用os.environ.get('key')
print( os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

#当前路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('D:\dmtest\PythonBasalArrangement\py3.6', 'testdir'))
#然后创建一个目录:
os.mkdir(r'D:\dmtest\PythonBasalArrangement\py3.6\testdir')
#删除一个目录
os.rmdir(r'D:\dmtest\PythonBasalArrangement\py3.6\testdir')

#拆分路径
print(os.path.split('/Users/michael/testdir/file.txt'))
#得到文件扩展名
print(os.path.splitext('/path/to/file.txt'))

#对文件重命名
#os.rename('test.txt', 'test.py')
#删除文件
#os.remove('test.py')

#列出当前目录下的所有目录
#isdir(path)为什么可以直接x不会报错，参数不是path么？
print([x for x in os.listdir('.') if os.path.isdir(x)])
#列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

