#!/usr/bin/env python3  

SEX_ARRAY = (['M','F'])

## 输入性别
def inputSex() :
	value = input("请输入您的性别（男性请输入M / 女性请输入F）：")
	if value.upper() in SEX_ARRAY :
		return value
	else :
		print("您输入的性别信息有误，请重新输入")
		inputSex()

## 输入腰围
def inputWaistLine():
	return float(input("请输入您的腰围（cm）："))
		
## 输入体重
def inputWeight():
	return float(input("请输入您的体重（kg）："))

## 计算体脂率
def calculateFatRat(waistline,weight,sex):
	if sex.upper() == 'M':
		x = 44.74
	elif sex.upper() == 'F':
		x = 34.89
	else :
		raise TypeError("bad operand type")
		
	a = waistline * 0.74
	b = weight * 0.082 + x
	return round((a - b) / weight , 4)

## 输出提示
def promptInfomation(fatRate,sex):
	if sex.upper() == 'M':
		if fatRate >= 0.26 :
			fatLevel = "肥胖"
		elif fatRate >= 0.18 :
			fatLevel = "可接受"
		elif fatRate >= 0.14 :
			fatLevel = "健康"
		elif fatRate >= 0.06 :
			fatLevel = "运动员"
		elif fatRate >= 0.02 :
			fatLevel =  "必要脂肪"
		else :
			fatLevel = "参数输入不正确，请确定参数单位"
			
	elif sex.upper() == 'F':
		if fatRate >= 0.32 :
			fatLevel = "肥胖"
		elif fatRate >= 0.25 :
			fatLevel = "可接受"
		elif fatRate >= 0.21 :
			fatLevel = "健康"
		elif fatRate >= 0.14 :
			fatLevel = "运动员"
		elif fatRate >= 0.1 :
			fatLevel =  "必要脂肪"
		else :
			fatLevel = "参数输入不正确，请确定参数单位"
		
	else :
		raise TypeError("bad operand type")
	
	return fatLevel

	
sex = inputSex()
waistline = inputWaistLine()
weight = inputWeight()
fatRate = calculateFatRat(waistline, weight , sex)

print("您的体脂率为：%.2f%% " % (fatRate * 100)," 您的体脂率级别为：",promptInfomation(fatRate,sex))
