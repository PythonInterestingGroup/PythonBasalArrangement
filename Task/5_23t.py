#!/usr/bin/Python
# coding=utf-8
a=['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']

m=[]
n=[]
result={}

for i in a:
	for im in i:
		m.append(im)
		if im not in n:
			n.append(im)

for x in n:
	num=0
	for y in m:
		if x == y:
			num=num+1
			result[x]=num
			
print result