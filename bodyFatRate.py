print("来计算下自己的体脂率吧，了解自己的体脂率能帮助我们决定自己的减肥目标是否切合实际")
sex = input("请输入你的性别：")
waistline = float(input("请输入你的腰围(cm)："))
weight = float(input("请输入你的体重（Kg）:"))
result = ''
if (sex == "女"):
    a = waistline * 0.74
    b = weight * 0.082 + 34.89
    fat = a - b
    bodyFatRate = (fat / weight) * 100
    if bodyFatRate >= 32:
        result = '肥胖，该减肥啦'
    elif (bodyFatRate >= 25) and (bodyFatRate < 32):
        result = '可接受'
    elif (bodyFatRate >= 21) and (bodyFatRate < 25):
        result = '健康，恭喜'
    elif (bodyFatRate >= 14) and (bodyFatRate < 21):
        result = '运动员体脂，太棒啦'
    elif (bodyFatRate >= 10) and (bodyFatRate < 14):
        result = '必要脂肪，不能再低啦'
    else:
        result = '体脂太低啦，快补补吧'
else:
    a = waistline * 0.74
    b = weight * 0.082 + 44.74
    fat = a - b
    bodyFatRate = (fat / weight) * 100
    if bodyFatRate >= 26:
        result = '肥胖，该减肥啦'
    elif (bodyFatRate >= 18) and (bodyFatRate < 26):
        result = '可接受'
    elif (bodyFatRate >= 14) and (bodyFatRate < 18):
        result = '健康，恭喜'
    elif (bodyFatRate >= 6) and (bodyFatRate < 14):
        result = '运动员体脂，太棒啦'
    elif (bodyFatRate >= 2) and (bodyFatRate < 6):
        result = '必要脂肪，不能再低啦'
    else:
        result = '体脂太低啦'

print('您的脂肪总重量为：' + str(round(fat, 2)) + 'kg,\n您的体脂率为：' + str(round(bodyFatRate, 2)) + '%', '体脂范围属于：' + result)
