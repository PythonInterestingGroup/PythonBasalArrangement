# -*- codeing: utf-8 -*-
# coding=utf-8
# pip install Pillow安装第三方库：基于PIL的Pillow项目，图像处理

# 其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2
from PIL import Image

im = Image.open("test.jpg")
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')
# 生成缩略图


import sys

print(sys.path)
# 添加模考搜索路径，这种方法是在运行时修改，运行结束后失效。
# sys.path.append('/Users/michael/my_py_scripts')
