#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      tingting.lu
#
# Created:     23/05/2017
# Copyright:   (c) tingting.lu 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
type = sys.getfilesystemencoding()


def femaleBFR(x,y):
   # print x,y
    a = float(x)*0.74
    b=float(y)*0.082+34.89
    c=a-b
    bodyFatRate=round(c/b,2)
    return bodyFatRate

def maleBFR(x,y):
    a = float(x)*0.74
    b=float(y)*0.082+44.74
    c=a-b
    bodyFatRate=round(c/b,2)
    return bodyFatRate



if __name__ == '__main__':
##    print("please enter your sex:Female/Male")
##    sex=input()
##    print("please enter your waist(cm):")
##    waist=input()
##    print("please enter your weight(kg):")
##    weight=input()

    sex = raw_input("sex:")
    waist = raw_input("waist:")
    weight = raw_input("weight:")

    if(sex=="female"):
        bodyFatRate=femaleBFR(waist,weight)
       # print bodyFatRate
        if(0.1<=bodyFatRate<=0.13):
            print "your BFR is:",bodyFatRate*100,"%必要脂肪".decode('UTF-8').encode(type)
        elif(0.14<=bodyFatRate<=0.13):
             print "your BFR is:",bodyFatRate*100, "%..您是运动员的水平".decode('UTF-8').encode(type)
        elif(0.21<=bodyFatRate<=0.24):
             print "your BFR is:",bodyFatRate*100,"%..您处于健康水平".decode('UTF-8').encode(type)
        elif(0.25<=bodyFatRate<=0.31):
             print 'your BFR is:',bodyFatRate*100,"%..您处在正常水平".decode('UTF-8').encode(type)
        elif(bodyFatRate>=0.32):
             print "your BFR is:",bodyFatRate*100,"%..您已经处于肥胖状态啦".decode('UTF-8').encode(type)
        else:
            print "数据有问题".decode('UTF-8').encode(type)
    else:
        bodyFatRate= maleBFR(waist,weight)
        if(0.02<= bodyFatRate<=0.05):
            print "your BFR is:",bodyFatRate*100,"%必要脂肪".decode('UTF-8').encode(type)
        elif(0.06<=bodyFatRate<=0.13):
             print "your BFR is:",bodyFatRate*100,"%您是运动员的水平".decode('UTF-8').encode(type)
        elif(0.14<= bodyFatRate<=0.17):
             print "your BFR is:",bodyFatRate*100,"%您处于健康水平".decode('UTF-8').encode(type)
        elif(0.18<=bodyFatRate<=0.25):
             print "your BFR is:",bodyFatRate*100,"%您处于可接受的范围".decode('UTF-8').encode(type)
        elif(bodyFatRate>=0.26):
             print "your BFR is:",bodyFatRate*100,"%您已经处于肥胖状态啦".decode('UTF-8').encode(type)
        else:
            print "数据有问题".decode('UTF-8').encode(type)
