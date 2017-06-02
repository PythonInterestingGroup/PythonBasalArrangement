import urllib
import urllib2
import cookielib

cookies = cookielib.MozillaCookieJar()
cookieHandler = urllib2.HTTPCookieProcessor(cookiejar=cookies)
opener = urllib2.build_opener(cookieHandler)
urllib2.install_opener(opener)

postData = {
    "remember": 1,
    "username": "1084933098@qq.com",
    "password": "l31415926"
}
headers = {
    "Accept": "*/*",

    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
    "Connection": "keep-alive",
    "Content-Length": "54",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_gat=1; PHPSESSID=YOUR_PHPSESSID; _ga=GA1.2.741059584.1485746441; Hm_lvt_e23800c454aa573c0ccb16b52665ac26=1485746441; Hm_lpvt_e23800c454aa573c0ccb16b52665ac26=1485746618",
    "DNT": "1",
    "Host": "segmentfault.com",
    "Origin": "https://segmentfault.com",
    "Referer": "https://segmentfault.com/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
request = urllib2.Request("https://segmentfault.com/api/user/login?_=57f36e7f98914cc9a7971aebc264e113", headers=headers)
request.add_data(urllib.urlencode(postData))

response = urllib2.urlopen(request)
print response.getcode()
for cookie in cookies:
    print cookie.name, cookie.value

response = urllib2.urlopen("https://segmentfault.com/u/charliecharlie")
print response.read()