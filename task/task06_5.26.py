#!/usr/bin/env python
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s,str)]