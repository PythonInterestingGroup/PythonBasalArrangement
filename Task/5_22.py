# coding:utf-8

sex=raw_input('输入性别\n')
c=input('请输入腰围（cm）')
weight=input('请输入体重（kg）')
b=1
if '男' in sex:
	print '男'
	b=weight*0.082+44.74
else:
	print '女'
	b=weight*0.082+34.89
result=c*0.74-b
print '你的体脂率是%.2f%%'%result


