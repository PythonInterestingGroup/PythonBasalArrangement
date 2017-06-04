#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      loretta
#
# Created:     02/06/2017
# Copyright:   (c) loretta 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#用 reduce 函数实现 map 函数的功能

from functools import reduce

L1 = [1,2,3,4,5,6,7,8,9]

def square_item(x , y) :
	if isinstance(x, list) :
		x.append(y * y)
		return x
	else :
		tempL = []
		tempL.append(x * x)
		tempL.append(y * y)
		return tempL

L2 = reduce(square_item, L1)


print("L1 :",L1)
print("L2 :",L2)

# 将一个二维数组内的每个数平方并且展平成一维数组
ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l2 = list((j * j for i in ll for j in i))


print("ll:",ll)
print("l2",l2)

