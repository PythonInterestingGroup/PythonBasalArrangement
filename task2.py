#/usr/bin/env python
#coding:utf-8
sex = raw_input('please input your Sex:')
waistline = raw_input('please input your Waistline:')
weight = raw_input('please input your Weight:')
if sex =='boy':
    BFR = (float(waistline)*0.74-(float(weight)*0.082+44.74))/float(weight)*100
    print 'Your BFR = ',BFR,'%'
    if float(BFR)>=2and float(BFR)<5:
        print '必要脂肪'
    elif float(BFR)>=6 and float(BFR)<13:
        print '运动员'
    elif float(BFR) >= 14 and float(BFR) < 17:
        print '健康'
    elif float(BFR)>=18 and float(BFR)<25:
        print '可接受'
    elif float(BFR)>=26:
         print '肥胖'
else:
    BFR = (float(waistline)*0.74-(float(weight)*0.082+34.89))/float(weight)*100
    print 'Your BFR = ',BFR,'%'
    if float(BFR)>=10 and float(BFR)<13:
        print '必要脂肪'
    elif float(BFR)>=14 and float(BFR)<20:
        print '运动员'
    elif float(BFR) >= 21 and float(BFR) < 24:
        print '健康'
    elif float(BFR)>=25 and float(BFR)<31:
        print '可接受'
    elif float(BFR)>=32:
         print '肥胖'
