# --*-- coding:utf-8 --*--
def AdviceM(rate):
	if 2 <= rate <= 5:
		print 'Necessary fat!!'
	elif 6 <= rate <= 13:
		print 'Athlete!'
	elif 14 <= rate <= 17:
		print 'Healthy!!'
	elif 18 <= rate <= 25:
		print 'Acceptable!!'
	else:
		print 'Fat!!'
		
def AdviceF(rate):
	if 10 <= rate <= 13:
		print 'Necessary fat!!'
	elif 14 <= rate <= 20:
		print 'Athlete!'
	elif 21 <= rate <= 24:
		print 'Healthy!!'
	elif 25 <= rate <= 31:
		print 'Acceptable!!'
	else:
		print 'Fat!!'

waist = raw_input('Please input your waist(cm): ')
weight = raw_input('Please input your weight(kg): ')
# temp variable
a = float(waist) * 0.74

gender = raw_input('Please input your gender(M/F): ')

if gender == 'M':
	# temp variable
	b = float(weight) * 0.082 + 44.74;
	fat = a - b
	rate = round(fat/b * 100, 2)
	print 'BRF is: %.2f%% ' %rate, AdviceM(rate)
elif gender == 'F':
	b = float(weight) * 0.082 + 34.89
	fat = a - b
	rate = round(fat/b * 100, 2)
	print 'BRF is: %.2f%%, you are ' %rate, AdviceF(rate)
else:
	print 'Error gender input!'
	