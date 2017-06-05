from functools import reduce

def square(x,y):
   if isinstance(x,list):
      t = x + [y*y]
   else:
      t = [x*x] + [y*y]
   return t

list1 = [1,2,3,4,5,6,7,8,9]   
print(reduce(square,list1))