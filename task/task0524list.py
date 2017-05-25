#!/usr/bin/env python
# -*- coding: utf-8 -*-

l=['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']

print l

count={}


for i in l:
    for ch in i:
        if ch in count:
            n=count[ch]
            count[ch]=n+1
        else:
            n=0
            count[ch]=1

print count
            
