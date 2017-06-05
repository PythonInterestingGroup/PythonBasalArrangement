#!/usr/bin/env python
# -*- coding: utf-8 -*-
print ord('a')
print chr(120)
print u'中文'
print u'中'
print u'\u4e2d'
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'
print 'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print u'\u4e2d\u6587'
print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('中文')
print 'hello,%s' % 'world'
print 'Hi,%s,you have $%d.' % ('DJX',10000000000)
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print '%2d-%02d' % (3,1)
print '%.2f' % 3.1415926
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print 'Age: %s. Gender： %s' % (25,True)
# ，用%%来表示一个%
print 'qrowth rate: %d%%' % 20
