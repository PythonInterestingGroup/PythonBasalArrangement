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
    Form_Data['salt'] = '1498113033183'
    Form_Data['sign'] = '7bb62c1ae096eaf0d40964e7d7fea4b7'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    Form_Data['typoResult'] = 'true'
    #使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(Request_URL,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用json
    translate_results = json.loads(html)
    #找到翻译结果{"translateResult":[[{"tgt":"杰克","src":"jack"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. 千斤顶；[电] 插座；男人\r\n","adj. 雄的\r\n","vt. 增加；提醒；抬起；用千斤顶顶起某物\r\n"],"type":1}}
    translate_results = translate_results['translateResult'][0][0]['tgt']
    #打印翻译信息
    print("翻译的结果是：%s"%translate_results)
