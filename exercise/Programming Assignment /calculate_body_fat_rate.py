#!/usr/bin/env python3  

##无方法一路到底版
sex = input("请输入您的性别（男性请输入M / 女性请输入F）：")


while sex.upper() != "M" and sex.upper() != "F" :
	print("您输入的性别信息有误，请重新输入")
	sex = input("请输入您的性别（男性请输入M / 女性请输入F）：")


waistline = float(input("请输入您的腰围（cm）："))
weight = float(input("请输入您的体重（kg）："))


if sex.upper() == "M" :
	a = waistline * 0.74
	b = weight * 0.082 + 44.74
	fatWeight = a - b
	fatRate = round( fatWeight / weight , 4 )
	
	if fatRate >= 0.02 and fatRate < 0.06 :
		fatLevel = "必要脂肪"
	elif fatRate >= 0.06 and fatRate < 0.14 :
		fatLevel = "运动员"
	elif fatRate >= 0.14 and fatRate < 0.18 :
		fatLevel = "健康"
	elif fatRate >= 0.18 and fatRate < 0.25 :
		fatLevel = "可接受"
	elif fatRate >= 0.26 :
		fatLevel = "肥胖"
	else :
		fatLevel = "参数输入不正确，请确定参数单位"
	
elif sex.upper() == "F" :
	a = waistline * 0.74
	b = weight * 0.082 + 34.89
	fatWeight = a - b
	fatRate = round( fatWeight / weight , 4 )
    
	if fatRate >= 0.1 and fatRate < 0.14 :
		fatLevel = "必要脂肪"
	elif fatRate >= 0.14 and fatRate < 0.21 :
		fatLevel = "运动员"
	elif fatRate >= 0.21 and fatRate < 0.25 :
		fatLevel = "健康"
	elif fatRate >= 0.25 and fatRate < 0.32 :
		fatLevel = "可接受"
	elif fatRate >= 0.32 :
		fatLevel = "肥胖"
	else :
		fatLevel = "参数输入不正确，请确定参数单位"
else :
	print("您输入的性别信息有误")



print("您的体脂率为：%.2f%% " % (fatRate * 100)," 您的体脂率级别为：",fatLevel)
