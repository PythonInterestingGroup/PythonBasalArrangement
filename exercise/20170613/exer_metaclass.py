#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hello import Hello
from hello import Hello2

h = Hello()
h.hello('ursus')

print("type(Hello):",type(Hello))
print("type(h):",type(h))


h2 = Hello2()
h2.hello('python')
print("type(Hello2):",type(Hello2))
print("type(h2):",type(h2))

# metaclass是类的模板，所以必须从`type`类型派生
class ListMetaclass（type):
	def __new__(cls,name,base,attrs):
		attrs['add'] = lambda self,value:self.append(value)
		return type.__new__(cls,name,bases,attrs)
		
class MyList(list,metaclass=ListMetaclass):
	pass