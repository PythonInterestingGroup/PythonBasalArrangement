#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# try.....except.......finally:
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print('try......')
    r = 10 / int('2')
    print('result:', r)
except ZeroDivisionError as e:  # except用来捕获错误
    print('zeroDevisionError:', e)
except ValueError as e:
    print('valueError:', e)
# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
else:
    print('no error')
finally:
    print('finally....')
print('end')

# 调用堆栈
# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# Python内置的logging模块可以非常容易地记录错误信息：
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('2')
    except Exception as e:
        logging.exception(e)


main()

print('i am tried')


# 抛出错误：raise
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    else:
        return 10 / n


foo('0')
