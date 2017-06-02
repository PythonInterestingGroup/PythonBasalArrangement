from functools import reduce
def prod(L):
    def multiply(x,y):
        return x*y
    return reduce(multiply,L)
L1 = [1,3,5,7,9]
print(prod(L1))
