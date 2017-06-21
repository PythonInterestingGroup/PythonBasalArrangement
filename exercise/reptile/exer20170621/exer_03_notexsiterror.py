# -*- coding:UTF-8 -*-

from urllib import request
from urllib import error

if __name__ == "__main__":

    url = "http://www.douyu.com/ursus.html"
    req = request.Request(url)
    try:
        response = request.urlopen(url)
    except error.URLError as e:
        if hasattr(e,'code'):
            print("HTTPError")
            print(e.code)
        elif hasattr(e,'reason'):
            print("URLError")
            print(e.reason)