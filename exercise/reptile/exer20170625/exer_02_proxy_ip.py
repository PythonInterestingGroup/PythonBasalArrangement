# -*- coding:UTF-8 -*-

from urllib import request

if __name__ == "__main__":
    url = 'http://www.xicidaili.com/'
    proxy={'http':'106.46.136.112:808'}
    proxy_support = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    request.install_opener(opener)
    response = request.urlopen(url)
    html = response.read().decode("utf-8")
    print(html)
