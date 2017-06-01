#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys
#sys模块有一个argv变量，用list存储了命令行的所有参数。
#argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：运行python3 hello.py获得的sys.argv就是['hello.py']；

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


#在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
#如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
    

#命令行运行
'''$python3 hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael'''

#命令行运行
'''$python3 hello.py
Hello, world!
$ python hello.py Michael
Hello, Michael'''


#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


def addFunc(a,b):  
    return a+b  
if __name__ == '__main__':
    print('learnmodule计算结果:',addFunc(1,1))
    
##注：name两边各有2个下划线__name__有2个取值：当模块是被调用执行的，取值为模块的名字；当模块是直接执行的，则该变量取值为：__main__
    
    

