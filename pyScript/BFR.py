# --*-- coding:utf-8 --*--

gender = raw_input('请输入性别(男/女)： ')
#print gender
waist = raw_input('请输入腰围(cm)： ')
weight = raw_input('请输入体重(kg)： ')

a = float(waist) * 0.74

if gender == '男':
	b = float(weight) * 0.082 + 44.74
	fat = a - b
	
elif gender == '女':
	b = float(weight) * 0.082 + 44.74
	fat = a - b
	#print '体脂率为: ', round(fat/b * 100, 2)

rate = round(fat/b * 100, 2)
print '体脂率为: ', rate 