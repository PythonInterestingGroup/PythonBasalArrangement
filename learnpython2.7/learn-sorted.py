#!/usr/bin/env python
# -*- coding: utf-8 -*-

#排序算法
#Python内置的sorted()函数就可以对list进行排序：
print sorted([2,3,6,1,98,101])

#sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序
#如果要倒序排序，我们就可以自定义一个reversed_cmp函数：
def resersed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0

print sorted([2,3,6,1,98,101],resersed_cmp)

#对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print sorted(['bob', 'about', 'Zoo', 'Credit'])

#排序应该忽略大小写，按照字母序排序
def cmp_ignore_case(s1,s2):
    u1=s1.upper()
    u2=s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

print sorted([36, 5, 12, 9, 21])[::-1]
#［::-1] 是个list的切片方法，步移为-1，从list的开始到最后,降序

#降序sorted([36, 5, 12, 9, 21], lambda x, y: y - x)
#sorted(['dsa','ADD','23','dfeeeee'], lambda x, y: cmp(y,x))


#排序过程
#第一次比较
#1：比较36，5  返回-1，不交换位置    36, 5, 12, 9, 21
#2：比较5，12  返回1，交换位置         36, 12, 5, 9, 21
#3：比较5，9     返回1，交换位置     36, 12, 9, 5, 21
#4：比较5，21     返回1，交换位置     36, 12, 9, 21, 5（此时最后的数为最小数）
#第二次比较
#1：比较36，12   返回-1  不交换位置   36, 12, 9, 21, 5
#2：比较12，9   返回-1  不交换位置   36, 12, 9, 21, 5
#3：比较9，21   返回1   交换位置   36, 12, 21,9, 5
#第三次比较
#1：比较36，12    返回-1   不交换位置   36, 12, 21,9, 5
#2：比较12，21     返回1，交换位置     36, 21, 12,9, 5
#第四次比较
#1：比较36，12   返回-1  不交换位置   36, 21, 12,9, 5
