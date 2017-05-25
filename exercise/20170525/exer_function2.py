###

def my_pow(x,n = 2):
	s = 1
	while n > 0 :
		n = n - 1
		s = s * x
	return s

print("2^8 =", my_pow(2, 8))

##默认参数的坑
def add_end( L = [] ):
	L.append('END')
	return L
print (add_end([1,23,45,6]))
print ("调用 add_end() :",add_end())
print ("再次调用 add_end() :",add_end())

# reason:Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
# 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

## 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！  


## 可变参数
def calc(*numbers):
	print(numbers)
	sum = 0
	for n in numbers :
		sum = sum + n * n
	return sum

print(calc(1,2,3))
print(calc(3,5,2,3))
print(calc(*(1,2,3,4,5,6,7)))

## 关键字参数
def person(name,age,**kw):
	if 'city' in kw:
		# 有city参数
		print("city exist")
		
	if 'job' in kw:
		# 有job参数
		print("job exist")
		
	print('name:',name,'age:',age,'ohter:',kw)
	
person('76',60, city='dld')
person('76',60, city='dld',weapon='gun')

extra = {'height':180,'weight':100}
person('76',60, **extra)

## 指定关键字
def student( name,age,*,grade,clazz):
	print('name:',name,'age:',age,'grade:',grade,'class',clazz)

student('xl', 10, grade = 5, clazz = 13)
student('xl', 10, clazz = 12, grade = 5)





	