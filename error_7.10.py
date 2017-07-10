#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from urllib import  error

# HTTPError -> URLError -> OSError

if __name__ == '__main__':
    url = 'http://www.douyu.com/Jack_Cui.html' # 不存在
    req = request.Request(url)
    try:
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    # except error.HTTPError as e:
    #     print('http reason: %s, code: %s' % (e.reason, e.code))
    # except error.URLError as e:
    #     print('url reason: %s, code: %s' % (e.reason, e.code))
    except error.URLError as e:
        if hasattr(e, 'code'): # 有 code 属性就是 HTTPError
            print('HTTPERROR')
            print(e.code)
        elif hasattr(e, 'reason'): # 有 reason 属性就是 URLError
            print('URLError')
            print(e.code)
