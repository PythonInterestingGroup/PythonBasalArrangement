#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
调用函数
'''
abs(-20)  # abs()求绝对值，参数只能有一个
print(abs(-20))
print(abs(122.455))

a = max(1, 2, 6, 0, 216, -19)
print(a)
a = min(1, 9, -9, 287, 8328, -2992)
print(a)

# 数据类型转换函数
print(int(12.34))
print(int('12663777'))
print(str(1123))
print(str('abc'))
print(float(123))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1))
b = int
print(b(12.34))

# 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串
a = hex(25)
b = str
print(b(a))

"""
定义函数
"""


# 自定义函数：def 函数名（参数）：
# print(type(123))
# print(type('qdbbc'))
# print(type(19.4636))
# print(isinstance(123, int))
# print(isinstance('abc', float))
# print(isinstance(123, (int, float)))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    elif x >= 0:
        return x
    else:
        return -x


print(my_abs(-9))
print(my_abs(11))

# print(my_abs('123'))

# 空函数，如果想定义一个什么事也不做的空函数，可以用pass语句
# age = int(input("请输入你的年龄："))
# if age > 10:
#     pass


import math


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)  # angle单位是弧度 360度=2π弧度
    ny = y + step * math.sin(angle)
    return nx, ny


r = move(0, 0, 5, math.pi / 6)
print(r)
h = math.radians(90)  # radians()把度转换为弧度
print(h)

# practice2
# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数


a = float(input('请输入a的值：'))
if a == 0:
    print('a的值不能为零，请重新输入')
    a = float(input('请输入a的值：'))
b = float(input('请输入b的值：'))
c = float(input('请输入c的值：'))

def quadratic(a, b, c):
    predic = b * b - 4 * a * c
    if predic >= 0:
        edu1 = (-b + math.sqrt(predic)) / 2 * a
        edu2 = (b + math.sqrt(predic)) / 2 * a
        print('%fx2 + %fx + %fc = 0的跟为：%.3f,%.3f' % (a, b, c, edu1, edu2))
    else:
        print("该一元二次方程无实根")
quadratic(a, b, c)





