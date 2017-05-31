# def count():
#     fs = []
#     for i in range(1, 4):
#         def f(j):
#              return j*j*j
#         fs.append(f(i))
#     return fs

# f1,f2,f3 = count()
# print f1,f2,f3

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f())
#     return fs

# f1, f2, f3 = count()
# print f1,f2,f3


# def count():
# 	fs=[]
# 	for i in xrange(1,4):
# 		def f():
# 			# def g():
# 			# 	return i*i
# 			# return g
# 			j=i
# 			return j*j
# 		fs.append(f)
# 	return fs
# f1,f2,f3=count()
# print f1(),f2(),f3()

# def count_2():
# 	fs=[]
# 	for i in xrange(1,4):
# 		def f(j):
# 			return lambda:i*j
# 		fs.append(f(i))
# 	return fs
# f1,f2,f3=count_2()
# print f1(),f2(),f3() 

# def count_2():
# 	fs=[]
# 	for i in xrange(1,4):
# 		def f(j):
# 			def g():
# 				print str(i)+'*'+str(j)
# 				return i*j
# 			return g
# 		fs.append(f(i))
# 	return fs
# f1,f2,f3=count_2()
# print f1(),f2(),f3()

f1, f2,f3 = [(lambda i = j : i*i) for j in range(1, 4)]
print f1(),f2(),f3()
# def count2():
# 	fs=[]
# 	for i in xrange(1,4):
# 		def f(j):
# 			return j*j
# 		fs.append(f(i))
# 	return fs
# f1,f2,f3=count2()
# print f1(),f2(),f3()
# def  sumT():
# 	i=1
# 	j=i
# 	return j
# for x in xrange(1,10):
# 	i=x
# 	print i
