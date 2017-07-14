# -*- coding: utf-8 -*-
#author dm

#在程序运行的过程中，所有的变量都是在内存中
#把变量从内存中变成可存储或传输的过程称之为序列化,pickling
#把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

import pickle
#写入文件
'''
d=dict(name='Bob', age=20, score=88)
pickle.dumps(d)  #把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
f = open('dump.txt', 'wb')
pickle.dump(d, f)   #pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()
'''
#从文件读取变量
#可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
f = open('dump.txt', 'rb')
d=pickle.load(f)
f.close()
print(d)

#JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))  #dumps()方法返回一个str，内容就是标准的JSON。

#类似的，dump()方法可以直接把JSON写入一个file-like Object。
#f=open('dumpjson.txt', 'w')
#json.dump(d,f)
#f.close()

#把JSON反序列化为Python对象，用loads()或者对应的load()方法
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

#json进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
#print(json.dumps(s))  报错
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
#通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__))

#要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))


