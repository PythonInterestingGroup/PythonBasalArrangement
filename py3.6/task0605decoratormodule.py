
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#1.通过装饰器测试出一个方法的执行耗时（在方法执行完成后打印: 方法名 耗时：xxxx(毫秒)）
#2.不使用语法糖（python的 @ 语法），完成上述任务

#time模块见learnmoduletime.py

import time
import functools

def exetime(func):
    @functools.wraps(func)
    def time1(*args,**kw):
        print('%s,start funtion %s'%(time.strftime('"%Y-%m-%d %X"',time.localtime()),func.__name__))
        #print('%s,start funtion %s'%(time.strftime('"%Y-%m-%d %X"'),func.__name__)) 同上        
        t1=time.time()
        #print('%s,start funtion %s'%(time.ctime(t1),func.__name__)) 等价
        back=func(*args,**kw)
        t2=time.time()
        print('%s,end funtion %s'%(time.strftime('"%Y-%m-%d %X"',time.localtime()),func.__name__))
        print("%.10fs taken for function %s" %(t2 - t1, func.__name__))
        return back
    return time1
'''
@exetime
def fibo(n):
    x,y=0,1
    i=0
    while i<n:
        x,y=y,x+y
        i=i+1
    #while(n):
        #x,y,n = y, x+y, n - 1        
    return '第%s个数值为：%s'%(n,x)
print(fibo(3000))
'''

#格式化：
#time.time()---time.ctime方法 "2017-06-01 11:02:37"
#time.localtime()--time.strftime方法 Thu Jun  1 11:02:37 2017


#1

@exetime
def _private_now():
    print('test execute time')
if __name__=='__main__':
    print('function1',_private_now())

'''
#2
def now1():
    print('test execute time')
now1=exetime(now1)

print('dunction2',now1())
'''
