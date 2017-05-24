## =================  list  ====================
print('=================  list  ====================')
## 类比java中的 List
## 有序集合，可以随时添加和删除

doubi = ['ljh','dbw','zwx']
print (doubi)

print ("逗比的个数：",len(doubi))
print ("第一个逗比：",doubi[0])
print ("最后一个逗比：",doubi[-1])

## append 往结尾添加
doubi.append('tjk')
print ("doubi.append('tjk'): %s"%(doubi))

## pop() 取出最后一个， pop(index) 取出对应下标的那个
print ("doubi.pop():  %s  -->  %s"%(doubi,doubi.pop()))

## list内的元素类型不定,元素可以是list
l1 = ['A',2,'J','Q','K','joker']
print (l1)
l2 = ['A',[2,3,4,5,6,7,8,9,10],['J','Q','K'],['joker','JOKER']]
print ("L2= %s \nL2[3][0]= %s"%(l2,l2[3][0]))

## 空list
l0 = []
print(l0)

## =================  tuple  ====================
print('\n\n=================  tuple  ====================')
## 类比java中的 final 数组
## tuple一旦初始化就不能修改
shadiao = ('lmd','tfq','jx')
print (shadiao)

## 单元素元组
singleT = (1,)
print (singleT)

## 可变元组
t1 = ('a','b',['A','B'])
print("T1=",t1)
t1[2][0] = 'C'
t1[2][1] = 'D'
print("执行t1[2][0] = 'C' 和 t1[2][1] = 'D'后，T1 =",t1)

## =================  dict  ====================
print('\n\n=================  dict  ====================')
score = {'SKT':100
,'WE':80
,'G2':85
,'FW':75
,'TSM':65
,'GAM':60}
print("score =",score,"\nscore['WE'] =",score['WE'])

score['WE'] = 84
print("执行score['WE'] = 84\nscore =",score)

score['RNG'] = 80
print("执行score['RNG'] = 80\nscore =",score)

print("score.get('EDG',79) =",score.get('EDG',79))
print("score.pop('GAM') =",score.pop('GAM'),"\nscore =",score)

## =================  set  ====================
print('\n\n=================  set  ====================')
s1 = set(['M','F'])
print (s1)
print ("'M' in s1 :",'M' in s1)

s2 = set(['M','F','M','F','M','F'])
print ("s2 = set(['M','F','M','F','M','F'])\ns2 =",s2)

s2.add('N')
print ("s2.add('N') ==> s2 =",s2)

print (s1 == s2)

print ("s1 & s2 =",s1 & s2)
print ("s1 | s2 =",s1 | s2)