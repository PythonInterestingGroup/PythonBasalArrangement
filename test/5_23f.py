#!/usr/bin/Python
# coding=utf-8
a=['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']

b=[]
for i in a:
    b.append(list(i))
print b

c=[]
for bm in b:
	for x in bm:
		c.append(x)
print c
d=[]
for x in c:
	if x not in d:
		d.append(x)

result={}
for x in d:
	num=0
	for n in c:
		if x == n:
			num=num+1
			result[x]=num
print result
m=[]
for i in a:
	for im in i:
		m.append(im)
print m	