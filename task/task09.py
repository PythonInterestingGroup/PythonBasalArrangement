#!/usr/bin/env python
#-*- coding:utf-8 -*-
#通过装饰器测试出一个方法的执行耗时（在方法执行完成后打印: *方法名* 耗时：xxxx(毫秒)）

import  functools
import time
def mylog_text(str):
    def mylog(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
             print func.__name__,'fuction is Starting...'
             start = time.time()
             f = func(*args,**kw)
             end = time.time()
             print func.__name__,'fuction is Ending...'
             print '%s的%s() 耗时：%.10f毫秒' % (str,func.__name__,(end-start)*1000)
             return f
        return wrapper
    return mylog
@mylog_text('djx')
def g(x):
    return x*x
print g(10000)

# 不使用语法糖（python的 @ 语法），完成上面问题

def k():
    return "test"
m= mylog_text('djx')(k)
print m()

