#-*-coding:utf-8-*-

print '了解你的体脂率(身体脂肪率）也能帮助你决定你的减肥目标是否实际。请记得，减肥不等于减少体重'
sex=raw_input('please input your sex: female or male \n')
print sex
waistline=input('please input your waistline/cm: \n')
weight=input('please input your weight/kg: \n')
  

if sex=='female':
    a=waistline*0.74
    b=weight*0.082+34.89
    c=a-b
    d=c/b
    print '你的体脂率为：',d*100,'%'
    if d<0.14:
        print '您的脂肪率分类为：必要脂肪'
    elif d>=0.14 and d<0.21:
        print '您的脂肪率分类为：运动员'
    elif d>=0.21 and d<0.25:
        print '您的脂肪率分类为：健康'
    elif d>=0.25 and d<0.32:
        print '您的脂肪率分类为：可接受'
    else:
        print '您的脂肪率分类为：肥胖'    

if sex=='male':
    a=waistline*0.74
    b=weight*0.082+44.74
    c=a-b
    d=c/b
    print '你的体脂率为：',d*100,'%'
    if d<0.06:
        print '您的脂肪率分类为：必要脂肪'
    elif d>=0.06 and d<0.14:
        print '您的脂肪率分类为：运动员'
    elif d>=0.14 and d<0.18:
        print '您的脂肪率分类为：健康'
    elif d>=0.18 and d<0.26:
        print '您的脂肪率分类为：可接受'
    else:
        print '您的脂肪率分类为：肥胖'

