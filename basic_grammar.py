item_one = 1
item_two = 2
item_three = 4
print("Hello,Python!");
if True:
    print("1")
else:
    print("2")
total = item_one + \
        item_two + \
        item_three
print(total)
item_four = 4.5
print(item_four)
item_five = "name"
print(item_five)
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)
word = 'word'
sentence = "这个是句子"
paragraph = """这个一个锻炼减
肥的护肤的后宫胡会号兑付号回复丢电话回访电话"""
print(paragraph)
print(sentence)
print(word)
# 注释
'''
三个单引号注释
'''
"""
三个双引号注释
"""
# world = input("\n\nPress the enter key to exit")
# print(world)
# a = input("press number a ")
# b = input("press number b")
# c = a + b
# print(c)
d = e = f = 1
print(d, e, f)
a, b, c = 2, 'string', 4.5
print(a, b, c)
# del d
# print(d)
s = 'abcdefg'
print(s[3:5])
'''
输出I'm "OK"!,使用转义字符\,在字符串的’和“前面分别加上\
'''
print('I\'m\"0k\"!')

"""
转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\,Python还允许用r''表示''内部的字符串默认不转义
如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''  '''的格式表示多行内容
"""
print('I am ok \nhello world')
print('i\t,,,,,,,,')
print('I\'m learning python,1\\2\\3')
print(r'happy a dog\\\\\\\\\\\\\\\\\\\n')
print('''line1
line2
line3''')
print('line1'
      'line2'
      'line3')
