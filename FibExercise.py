def Fib(max):
   n,a,b = 0,0,1
   while n<max:
         yield b
         a,b = b,a+b
         n  += 1
   return
n = input('please enter a number:')
for s in Fib(n): 
   print(s)
