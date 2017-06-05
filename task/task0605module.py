
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#斐波那契数列:起始两项为0和1，此后的项分别为它的前两项之后。


import sys
sys.path.append('D:\dmtest\PythonBasalArrangement\py3.6')

import task0605decoratormodule


@task0605decoratormodule.exetime
def fibo(n):
    x,y=0,1
    i=0
    while i<n:
        x,y=y,x+y
        i=i+1
    #while(n):
        #x,y,n = y, x+y, n - 1        
    return x
print('斐波那契数列:',fibo(1000))


#@task0605decoratormodule.exetime
#def testfibo():
#    print ('斐波那契数列fibo100:',fibo(100))
#testfibo()    

