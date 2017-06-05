#!/usr/bin/env python
mylist = ['adam', 'LISA', 'barT']


def f(l):
    return l[0].upper() + l[1:].lower()


print map(f, mylist)

myList1 = [1, 2, 3, 4, 5, 6, 7, 8]


def prod(x, y):
    return x * y


reduce(prod, myList1)

import math

l = range(1, 101)


def delete_sushu(num):
    if num == 1:
        return num
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return num


print filter(delete_sushu, l)


def g(l):
    lis1 = []
    for x in l:
        lis2 = []
        lis2.append(x)
        lis2.append(x)
        lis1.append(reduce(f, lis2))
    return lis1


L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print g(L)

myL = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def myL_m(l):
    nl = []
    for s in l:
        for y in s:
            nl.append(y)


def myL_n(x):
    return x * x


print list(map(myL_n, myL_m(myL)))