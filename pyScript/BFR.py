# --*-- coding:utf-8 --*--

gender = raw_input('�������Ա�(��/Ů)�� ')
#print gender
waist = raw_input('��������Χ(cm)�� ')
weight = raw_input('����������(kg)�� ')

a = float(waist) * 0.74

if gender == '��':
	b = float(weight) * 0.082 + 44.74
	fat = a - b
	
elif gender == 'Ů':
	b = float(weight) * 0.082 + 44.74
	fat = a - b
	#print '��֬��Ϊ: ', round(fat/b * 100, 2)

rate = round(fat/b * 100, 2)
print '��֬��Ϊ: ', rate 