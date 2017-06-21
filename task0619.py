from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)  #{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}