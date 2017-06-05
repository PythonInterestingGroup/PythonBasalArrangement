#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 现有list a=['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']
# 计算出a中每个字母出现次数,并以dict形式打印出来,如:
# {'a': 7, ' ': 7, 'e': 4, 'd': 2, 'g': 8, 'i': 7, 'h': 2, 'j': 1, 'm': 1, 'l': 2, 'o': 5, 'n': 6, 'p': 1, 's': 5, 'r': 1, 'u': 2, 'y': 3, 'x': 1}

a=['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']
b=''
for str in a:
    b =b+str
setA = set([])
for c in b:
    setA.add(c)
dictA = {}
for c in setA:
    cout =0;
    for d in b:
        if c==d:
            cout +=1
    dictA[c] = cout
print 'result =',dictA

