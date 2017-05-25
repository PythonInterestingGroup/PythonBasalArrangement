# _*_ coding: utf-8 _*_
def sex():
	while True:
		sex = raw_input("选择您的性别M(男)/F(女)：")
		if sex.lower() == "f":
			return "f"
		elif sex.lower() == "m":
			return "m"
		else :
			print("请选择正确的性别！")
			continue 


def width():
	l = raw_input("请输入您的腰围(cm)：")
	return float(l)
def weight():
	w = raw_input("请输入您的体重（kg）：")
	return float(w)

s = sex()
l = width()
w = weight()
a = float(l) * 0.74
b = 0.0
if s == "m":
	b = w * 0.082 + 44.74
elif s == "f":
	b = w * 0.082 + 34.89
total = a - b
rate = total/w *100
print("您的体脂率为：%.2f%%"%rate)
if s == "m":
	if rate > 32:
		print("肥胖，注意减肥")
	elif rate > 25:
		print("可接受，瘦一点更美哦")
	elif rate > 21:
		print("您很健康，注意保持")
	elif rate > 14:
		print("哇，您拥有运动员的的身体")
	else :
		print("您太瘦了，注意营养哦")
elif s == "f":
	if rate > 26:
		print("肥胖，注意减肥")
	elif rate > 18:
		print("可接受，瘦一点更美哦")
	elif rate > 14:
		print("您很健康，注意保持")
	elif rate > 6:
		print("哇，您拥有运动员的的身体")
	else :
		print("您太瘦了，注意营养哦")