#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from io import StringIO
f = StringIO()
f.write('hello world!')

print(f.getvalue())

from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break;
	print(s.strip())
	