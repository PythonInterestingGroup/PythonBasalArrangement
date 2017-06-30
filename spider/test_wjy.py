from urllib import request
from urllib import parse
import json

if __name__ == '__main__':
    Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
    Form_Data = {}
    Form_Data['i'] = 'jack'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1498112341468'
    Form_Data['sign'] = 'ccbabcc04df776d1f3d27b03c78b644b'
    Form_Data['version'] = '2.1'
    Form_Data['keyform'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    Form_Data['typoResult'] = 'true'

    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print("翻译的结果是：%s"%translate_results)
'''
    data = parse.urlencode(Form_Data).encode('utf-8')   #使用urlencode方法转换标准格式
    response = request.urlopen(Request_URL, data)
    html=response.read().decode('utf-8')
    translate_results=json.loads(html)
    translate_results=translate_results['translateResult'][0][0]['tgt']  #找到翻译结果
    print("翻译的结果是：%s" % translate_results)
'''
from urllib import request
from urllib import parse
import json

if __name__ == '__main__':
    Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
    Form_Data = {}
    Form_Data['i'] = 'jack'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1498112235489'
    Form_Data['sign'] = 'edb8af13f44e1f8c5c58896d999c53ac'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    Form_Data['typoResult'] = 'true'

    data = parse.urlencode(Form_Data).encode('utf-8')

    response = request.urlopen(Request_URL,data)

    html = response.read().decode('utf-8')

    translate_results = json.loads(html)
    print("结果是：%s" % translate_results)
    translate_results = translate_results['translateResult'][0][0]['tgt']

    print("翻译的结果是：%s"%translate_results)
