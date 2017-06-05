#!/usr/bin/env python

def count_v1():
    fs = []
    for i in range(1, 4):
        fs.append(lambda i:i * i)
        return fs

    f1, f2, f3 = count_v1()
    print("f1:", f1(), "f2:", f2(), "f3:", f3())

    def count_v2():
        f = lambda j:j * j
        fs = []
        for i in range(1, 4):
            fs.append(f(i))
        return fs

    f4, f5, f6 = count_v2()
    print("f4:", f4(), "f5:", f5(), "f6:", f6())