#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('angry-birds.png')
print('type(im):',type(im))
print(im.format, im.size, im.mode)

im.thumbnail((128,128))
im.save('angry-birds-128.png')



