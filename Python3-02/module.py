# _*_ coding:utf-8 _*_

'use module'

__author__ = "Tan"

import sys

def test():
	args = sys.argv #sys模块有个 argv 保存命令行的所有参数 切至少有一个元素 文件名
	if  len(args) == 1:
		print("Hello, %s"%args[0])
	elif len(args) == 2:
		print("Hello, %s"%args[1])
	else :
		print("too many args")


# 直接运行模块文件时, Python 会把一个特殊的变量 __name__置为__main__
# 而其他模块导入该模块时,此 if 判断将会失败
if __name__=='__main__': 
	test()

# 类似 _a __a 的变量被认为是 private 属性的, 不应该被外界引用

# from PIL import Image

# im = Image("tuzi.jpg")
# print(im.format, im.size, im.mode)