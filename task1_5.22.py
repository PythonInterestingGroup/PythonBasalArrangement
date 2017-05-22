
waistline = input("请输入你的腰围(cm):")
weight = input(" 请输入你的体重(kg):") 
sex = input("请输入你的性别, 女生 Y,男生 N. Y/N?")

a = 0
b = 0
fat = 0
fatRate = 0

def female():
	global fatRate
	a = float(waistline) * 0.74
	b = float(weight) * 0.082 + 34.89
	fat = a - b
	fatRate = fat / float(weight)
def male():
	global fatRate
	a = float(waistline) * 0.74
	b = float(weight) * 0.082 + 44.74
	fat = a - b
	fatRate = fat / float(weight)

def sexAction():
	global sex

	if sex.upper() == 'Y':
		female()
	elif sex.upper() == 'N':
		male()
	else:
		sex = input("性别输入错误,请重新输入, 女生:Y,男生:N, Y/N?")
		sexAction()


sexAction()

result = format(fatRate, '0.2%')
print("您的体脂比是: %s" % result)

def femaleDes(rate):
	if 0.1 <= rate and 0.13 >= rate:
		print("必要脂肪")
	elif 0.14 <= rate and 0.20 >= rate:
		print("运动员")
	elif 0.21 <= rate and 0.24 >= rate:
		print("健康")
	elif 0.25 <= rate and 0.31 >= rate:
		print("可接受")
	elif 0.32 <= rate:
		print("肥胖")
	else:
		print("你可能是个死人")

def maleDes(rate):
	if 0.02 <= rate and 0.05 >= rate:
		print("必要脂肪")
	elif 0.06 <= rate and 0.13 >= rate:
		print("运动员")
	elif 0.14 <= rate and 0.17 >= rate:
		print("健康")
	elif 0.18 <= rate and 0.25 >= rate:
		print("可接受")
	elif 0.26 <= rate:
		print("肥胖")
	else:
		print("你可能是个死人")



if sex.upper() == 'Y':
	femaleDes(fatRate)
else:
	maleDes(fatRate)


# 还是有很多可以抽离出来的地方....不过还不太理解 Python 中关于变量的域就暂且这样
# 