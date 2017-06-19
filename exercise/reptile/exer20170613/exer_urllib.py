# -*- coding: UTF-8 -*-

from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("https://github.com/UrsusMountain")
    html = response.read()
    charset = chardet.detect(html)
    print("charset:",charset)
    html = html.decode(charset.get('encoding','utf-8'))
    print(html)