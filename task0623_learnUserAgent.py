from urllib import request

if __name__ == '__main__':
    url = 'http://www.csdn.net'
    head = {}
    #д��User Agent��Ϣ
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #����request����
    req = request.Request(url,headers=head)
    #���봴���õ�Request����
    response = request.urlopen(req)
    #��ȡ��Ӧ��Ϣ������
    html = response.read().decode('utf-8')
    print(html)