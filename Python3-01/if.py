# _*_ coding:utf-8 _*_

text = input("请输入你的年龄:")
age = int(text)
if age >= 18:
    print("你是一个成年人,年龄:%s"%age)
elif age <= 12:
    print("你是一个未成年人,年龄:%s"%age)
else:
	print("你是一个青少年,年龄:%s"%age)


bmi = 63.5/(1.71*1.71)
result = "结果"
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

print("bmi 指数为:%.2f"%bmi,result)