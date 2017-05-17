#!/usr/bin/Python
#-*- coding: utf-8 -*-
import os
import sys
# 创建目录
def mkdir(path):

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    isExists=os.path.exists(path)
    if not isExists:
        print path+' 创建成功'
        os.makedirs(path)
        return True
    else:
        print path+' 目录已存在'
        return False
if __name__ == '__main__':

	path=os.path.split( os.path.realpath( sys.argv[0] ) )[0]  
	path=path+'/12344'
	# 调用函数
	mkdir(path)
	# 创建文件 有直接打开 没有则创建
	fo = open("%s/58222.txt"%(path), "wb")
	fo.write('1232213123asdada')
	fo.close()



