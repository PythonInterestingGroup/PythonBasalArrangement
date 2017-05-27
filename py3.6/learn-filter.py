# -*- coding: utf-8 -*-

#filter()也接收一个函数和一个序列,过滤序列

#过滤偶数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

#过滤空字符串
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#用用filter求素数
#用filter求素数
#先构造一个从3开始的奇数序列      
def _odd_iter():    
    n=1
    while True:
        n = n + 2
        yield n

#定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

#定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#字写
def not_sushu(n):
    for i in range(2,n):
        if n%i==0:
            #i=i+1
            return True
    return False
                 
#l=range(1,11) #[1,2,3,4,5,6,7,8,9,10]
l=range(1,100)
print (list(filter(not_sushu,l)))
