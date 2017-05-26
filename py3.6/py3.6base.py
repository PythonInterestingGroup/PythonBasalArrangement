#!/usr/bin/env python
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#input可输入任意字符，2.7input为数字类型

#name=input("please input your name:")
#print('hello,', name)

#练习输出：
print('1024*768=',1024*768)

#练习数据类型:
print('n=',123)
print('f=',456.789)
print('s1=',"'hello,world'")
print('s2=',"'hello,\\'Adam\\''")

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print('n=',n,'f=',f,'s1=',s1)
print('n = %d \nf = %.3f \ns1 = %s \ns2 = %s \ns3 = %s \ns4 = %s' %(n,f,s1,s2,s3,s4))

#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print ('%2d-%02d' % (3, 1))
print ('%.2f' % 3.1415926)


#break and continue
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
#break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

#练习
#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n=255
print(hex(n))

#数据类型检查
#n=input('please input a number:')
n='ab'
if not isinstance(n, (int, float)):
    print('please input right number')
else:
    print(n)

#练习函数：返回一元二次方程：ax2 + bx + c = 0的两个解。
import math
def quadratic(a, b, c):
    for i in [a,b,c]:
        if not isinstance(i, (int, float)):
            raise TypeError('bad operand type', i)
        m = b ** 2 - 4*a*c
        if m<0:
            print('方程无实根')
        elif m==0:
            print('方程只有一个实根')
            return -b/2*a
        else:
            x2 = (-b+math.sqrt(m))/2*a
            x3 = (-b-math.sqrt(m))/2*a
            print('方程有两个实根')
            return x2, x3
print(quadratic(1,4,3))

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：

def person(name, age, *, city, job):
    print(name, age, city, job)
    
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

print(person('Jack', 24, city='Beijing', job='Engineer'))

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
#命名关键字参数必须传入参数名
#命名关键字参数可以有缺省值，从而简化调用：

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
print(person('Jack', 24, job='Engineer'))

def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
y=f1(1, 2, 3, 'a', 'b', x=99)
x=f2(1, 2, d=99, ext=None)

#通过一个tuple和dict，你也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
z=f1(*args, **kw)

#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。

#练习列表生成式
#把一个list中所有的字符串变成小写，list中既包含字符串，又包含整数
L1= ['Hello', 'World', 18, 'Apple', None,'test']

L2 = [i.lower() for i in L1 if isinstance(i, str)]
print (L2)

