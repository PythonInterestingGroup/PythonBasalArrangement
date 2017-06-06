# --*-- coding: utf-8 --*--

'''
模块functools的用法
'''

import functools

## functools.partial创建偏函数
# functools.partital(func[, *args][, **keywords])
int2 = functools.partial(int, base = 2)

#def int2(x, base=2):
	#return int(x, base)

print 'Example for partial: ', int2('1000000')

## functools.update_wrapper
# functools.update_wrapper(wrapper, wrapped[, assigned][, updated])
# 
def _deco(func):
	def __deco(*args, **kw):
		print 'execute function %s.' % func.__name__
		return func(*args, **kw)
	return __deco

def _deco1(func):
	def __deco1(*args, **kw):
		print 'execute function %s.' % func.__name__
		return func(*args, **kw)
	return functools.update_wrapper(__deco1, func)

@_deco
def reading():
	'''Read the following sentences'''
	return 'Jacky is funny!'

print '\nBefore using update_wrapper:'
print reading()
print reading.__doc__
print reading.__name__

@_deco1
def reading():
	"Read the following sentences"
	return 'Jacky is funny!'

print '\nAfter using update_wrapper:'
print reading()
print reading.__doc__
print reading.__name__


print '\n Usage of wrapper:'
# 等价于partial(update_wrapper, wrapped = wrapped, assigned = assigned, updated = updated)
def _decoWraps(func):
	@functools.wraps(func)
	def __decoWraps(*args, **kw):
		print 'execute function %s.' % func.__name__
		return func(*args, **kw)
	return __decoWraps

@_decoWraps
def writing():
	"Write the following word!"
	return 'Lucy is nice.'

print writing()
print writing.__doc__

##