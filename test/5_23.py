#!/usr/bin/Python
# coding=utf-8
# a='liang'
# b=a.replace('l','j')
# c=b
# c.replace('a','A')


# b=[1,2,3,a]
# c=(1,2,3,b)
# b[2]='jiang'
# b.append('hao')

# d=set(b)
# d.add('5')

# # f={'a':a,'b':b,'c':c,'d':d}
# print d
# # f.append('hansome')
# # for fs in f:
# 	# print fs

# # print dict

# x=[1,[2,3],(4,5)]
# y=(1,2,3,4,b)
# x[2]=3
# # print b[2][1]
# # print a

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# # print(n)

# a=["abc","def","ghi"]
# print len(''.join(a))
#hansome singledog gaygayde
# a=["abc is soadjaw","def sdbee aasdawiiii sdjasd ","ghi sahdawaksdwidffg"]
a=['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']
count=0
# for i in a:
#     count+=len(i)
# print(count)
# b=set(a)
for i in a:
    count+=len(i)
# print(count)

b=[]
for i in a:
    b.append(list(i))
# print(b)

# print(len(b[0]))
c=[]
for bm in b:
	for x in bm:
		c.append(x)
# print c
# print len(c)

d=[]
for x in c:
	if x not in d:
		d.append(x)

# print d
# print len(d)


setC=set(c)

# print len(setC)
result={}

for x in d:
	num=0
	for n in c:
		if x == n:
			num=num+1
			result[x]=num
			# print x
			# print num


print result
	


