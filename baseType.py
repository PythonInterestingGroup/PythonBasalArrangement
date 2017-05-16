# 4 space or a tab
# Case-sensitive letters

# Interger

binaryInt = '1111' # 0b
decimalInt = '110'
octalIntt = '777' # 0o
hexInt = 'ffee' # 0x

print("16 => 10: ", int(hexInt, 16)) # int: arg1: 字符串类型, arg: 指定参数一的进制类型
print("8 => 10: ", int(octalIntt, 8))
print("2 => 10: ", int(binaryInt, 2))

print('===========================')

print("10 => 16: ", hex(1111)) # arg: 整型
print("2 => 16: ", hex(int(binaryInt, 2))) # 2 => 10 => 16
print("8 => 16: ", hex(int(octalIntt, 8)))

print('===========================')

print("10 => 2: ", bin(110)) # arg: 整型
print("16 => 2: ", bin(int(hexInt, 16))) # 16 => 10 => 2
print("8 => 2: ", bin(int(octalIntt, 8)))

print('===========================')

print("10 => 8: ", oct(100)) # arg: 整型
print("2 => 8: ", oct(int(binaryInt, 2))) # 2 => 10 => 8
print("16 => 8: ", oct(int(hexInt, 16)))

print('===========================')

# Float

# 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差
efloat = 2.188e9
fefloat = 2.188e-9

print(efloat)
print(fefloat)

print('===========================')

# String

uniqueString = " It's an unique string!"
print("uniqueString = ", uniqueString)
uniqueString02 = 'It\'s same as uniqueString'
print("uniqueString02 = ", uniqueString02)
print(r'\\\t\\') # 为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('''line1
...line2
...line3''') # 为了简化，Python允许用'''...'''的格式表示多行内容
print(r'''line1
...line2
...line3''')

# Bool

print(3 > 2)
print(3 < 2)

# None

# varieable

a = 'ASD'
b = a
a = 'ZXC'
print("b = ", b)

# constant
# 在Python中，通常用全部大写的变量名表示常量

# division

print(10 / 3)
print(10 // 3)
print(10 % 3)
