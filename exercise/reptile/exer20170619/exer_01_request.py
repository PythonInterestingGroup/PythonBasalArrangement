# -*- coding:utf-8 -*-

from urllib import request
import chardet

if __name__ == '__main__':
    req = request.Request('https://github.com/UrsusMountain')
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)
    html = html.decode(charset.get('encoding','utf-8'))
    print(html)