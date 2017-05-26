# --*-- coding:utf-8 --*--
def AdviceM(rate):
	if 2 <= rate <= 5:
		return 'Necessary fat!!'
	elif 6 <= rate <= 13:
		return 'Athlete!'
	elif 14 <= rate <= 17:
		return 'Healthy!!'
	elif 18 <= rate <= 25:
		return 'Acceptable!!'
        elif rate >= 26:
		return 'Fat!!'
        else:
            return 'Error'
		
def AdviceF(rate):
	if 10 <= rate <= 13:
		return 'Necessary fat!!'
	elif 14 <= rate <= 20:
		return 'Athlete!'
	elif 21 <= rate <= 24:
		return 'Healthy!!'
	elif 25 <= rate <= 31:
		return 'Acceptable!!'
        elif rate >= 32:
		return 'Fat!!'
        else:
            return 'Error!'
            #return 0

waist = raw_input('Please input your waist(cm): ')
weight = raw_input('Please input your weight(kg): ')
# temp variable
a = float(waist) * 0.74

gender = raw_input('Please input your gender(M/F): ')

if gender.upper() == 'M':
	# temp variable
	b = float(weight) * 0.082 + 44.74;
	fat = a - b
	rate = round(fat/b * 100, 2)
	print 'BRF is: %.2f%% ' %rate, AdviceM(rate)
elif gender.upper() == 'F':
	b = float(weight) * 0.082 + 34.89
	fat = a - b
	rate = round(fat/b * 100, 2)
	print 'BRF is: %.2f%% ' %rate, AdviceF(rate)
else:
	print 'Error gender input!'
	
