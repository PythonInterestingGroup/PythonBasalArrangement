
# _*_ coding:UTF-8 _*_


from urllib import request

if __name__ == "__main__":
	req = request.Request("http://fanyi.baidu.com/")
	response = request.urlopen(req)
	html = response.read()
	html = html.decode('utf-8')
	print(html)
