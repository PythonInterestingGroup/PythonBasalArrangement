# python运算符
# 1.算术运算符
# 2.比较运算符
# 3.赋值运算符
# 4.逻辑运算符
# 5.位运算符
# 6.成员运算符
# 7.身份运算符
# 8.运算符优先级

# 算术运算符：+ -  * / %  **  //
a = 5
b = 2
c = a + b  # (加)
print(c)
c = a - b  # （减）
print(c)
c = a * b  # （乘）
print(c)
c = a / b  # （除）
print(c)
c = a % b  # （取模）
print(c)
c = a ** b  # （幂）
print(c)
c = a // b  # （取整除）
print(c)

# 比较运算符：==  ！=  >  <  >=  <=
a, b, c = 21, 10, 0
if (a == b):
    print("1:a等于b")
else:
    print("1:a不等于b")
if (a != b):
    print("2:a不等于b")
else:
    print("2:a等于b")
# python 不支持<>
# if (a <> b):
#     print("3:a不等于b")
# else:
#     print("3:a等于b")
if (a > b):
    print("3:a大于b")
else:
    print("3:a小于等于b")
if (a < b):
    print("4:a小于b")
else:
    print("4:a大于等于b")

# 赋值运算符：=  +=  -=  *=  /=  %=  **= //=
a, b = 11, 10
c = a + b
c += a
print(c)
c -= b
print(c)
c *= a
print(c)
c /= b
print(c)
c %= a
print(c)
c **= a
print(c)
c //= b
print(c)

# 位运算符，是把数字看作二进制来进行计算 &（与） |（或）  ^(异或)  ~（取反） <<(左移)  >>(右移)
a, b = 60, 13
# a(2)=00111100
# b(2)=00001101
c = a & b  # a&b= 00001100(同为1，取1)
print(c)
c = a | b  # a|b=00111101（有一位为1，则取1）
print(c)
c = a ^ b  # a^b=00110001(对应的二进制相异，则取1)
print(c)
c = ~a  # ~a=11000011
print(c)
c = a << 2  # 运算数的各位全部左移若干位，高位丢弃，低位补0
print(c)
c = a >> 2  # 运算数的各位全部右移若干位，低位丢弃，高位补0
print(c)

# 逻辑运算符and  or  not
a = 10
b = 2

