#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata

print "了解你的体脂率(身体脂肪率）也能帮助你决定你的减肥目标是否实际。请记得，减肥不等于减少体重"

def sex():
    while True:
        sex=raw_input('please input your sex: f or m \n')
        if sex.upper()=='F':
            return 'f'
        if sex.upper()=='M':
            return 'm'
        else:
            print "please inpur right sex"
            continue

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    '''try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass'''
    return False

def waist():
    while True:
        waistline=raw_input('please input your waistline/cm: \n')
        if is_number(waistline):
            return float(waistline)
        else:
            print "please input right number"
            continue
    
    #error:NameError: global name 'ValueErrror' is not defined不是很理解
''' try:
        float(waistline)
        return float(waistline)
    except ValueErrror:
        pass
    return "please input right number"'''
   
    
    #错误，因为输入的永远是str
    #if isinstance(waistline,(int,float)):
       # return float(waistline)
    #return "please input right number"
    #isdigit()方法判断字符串是否为数字组成，整型

def weight():
    while True:
        weight=raw_input('please input your weight/kg: \n')
        if is_number(weight):
            return float(weight)
        else:
            print 'please input right number'
            continue

s=sex()
l=waist()
w=weight()

a=l*0.74
if s=='f':    
    b=w*0.082+34.89
elif s=='m':
    b=w*0.082+44.74
c=a-b
d=c/b
print '你的体脂率为：%.2f%%'%(d*100)
#print '你的体脂率为：',d*100,'%'

if s=='f':
    if d>0.32:
        print '您的脂肪率分类为：肥胖'
    elif d>0.25:
        print '您的脂肪率分类为：可接受'
    elif d>0.21:
        print '您的脂肪率分类为：健康'
    elif d>0.14:
        print '您的脂肪率分类为：运动员'
    else:
        print '您的脂肪率分类为：必要脂肪'

if s=='m':
    if d<0.06:
        print '您的脂肪率分类为：必要脂肪'
    elif d<0.14:
        print '您的脂肪率分类为：运动员'
    elif d<0.18:
        print '您的脂肪率分类为：健康'
    elif d<0.26:
        print '您的脂肪率分类为：可接受'
    else:
        print '您的脂肪率分类为：肥胖'
        
        
    
    







