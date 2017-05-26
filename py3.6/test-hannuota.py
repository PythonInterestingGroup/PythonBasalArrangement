#!/usr/bin/env python
# -*- coding: utf-8 -*-

#利用递归函数移动汉诺塔:
def move(n,a,b,c):
    if n==1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(4,'A','B','C')


'''这个游戏的规律：
一、把a上面的除最大的那个，剩下的其他盘(n-1 个)移动到b;
二、然后把a最后一个最大的移动到c上;
三、然后再把b上的移动到c上：
把b上除最大的盘子，剩下的其他盘(n-1 个)移动到空的a上，然后把b最大的移动到c上...'''
