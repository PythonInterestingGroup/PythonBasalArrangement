#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

s1 = 72.0
s2 = 85.0
r = s2/ s1 *100
print('小明今年的成绩85交去年的72提升了%.2f%%'%r)

height = 1.75
weight = 80.5
bmi = weight/(height*height)
result = ""
if bmi < 18.5:
    result = "过轻"
elif bmi < 25:
    result = "正常"
elif bmi < 28:
    result = "过重"
elif bmi < 32:
    result = "肥胖"
else:
    result = "严重肥胖"

print('bmi :%.2f'%bmi,result)

L = ['Bart', 'Lisa', 'Adam']
for nike in L :
	print("Hello %s"%nike)