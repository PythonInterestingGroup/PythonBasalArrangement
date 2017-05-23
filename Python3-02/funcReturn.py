# _*_ coding: utf-8 _*_

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

l = [1, 3, 5, 7, 9]
f = lazy_sum(1, 3, 5, 7, 9) # = lazy_sun(*l)
print(f())