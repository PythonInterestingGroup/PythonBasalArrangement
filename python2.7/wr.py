#!/usr/bin/Python
#-*- coding: utf-8 -*-
import os
import sys
# for letter in 'Python':     # 第一个实例
# for i in xrange(1,10):
# 	fo.write(str(i)
# fo.close()
SOLR_URL='test+'
# def globalT():
#     global SOLR_URL
    # SOLR_URL='test+'
def writeS(fo):
	# globalT()
	for i in xrange(1,10):

		for letter in 'Python':     # 第一个实例
			# print i
			global SOLR_URL
			SOLR_URL=SOLR_URL+str(i)+letter+'\n'
			fo.write(str(i)+letter+'\n')
	fo.close()
if __name__ == '__main__':
	fo=open('my.txt','wb')
	writeS(fo)

	print SOLR_URL
