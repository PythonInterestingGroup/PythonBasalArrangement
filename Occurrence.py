#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      loretta
#
# Created:     24/05/2017
# Copyright:   (c) loretta 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_times(list1):
    s="".join(list1)
    d=dict()
    for j in s:
        if j in d.keys():
            d[j]=d[j]+1
        else:
            d[j]=1
    return d



if __name__ == '__main__':
    a=['liangjianghao is hansome','xiongyue is single dog','pangruo is gaygayde']
    d=get_times(a)
    for (d,x) in d.items():
       print d+":"+str(x)




