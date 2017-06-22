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
    #ʹ��urlencode����ת����׼��ʽ
    data = parse.urlencode(Form_Data).encode('utf-8')
    #����Request�����ת�����ʽ������
    response = request.urlopen(Request_URL,data)
    #��ȡ��Ϣ������
    html = response.read().decode('utf-8')
    #ʹ��json
    translate_results = json.loads(html)
    #�ҵ�������{"translateResult":[[{"tgt":"�ܿ�","src":"jack"}]],"errorCode":0,"type":"en2zh-CHS","smartResult":{"entries":["","n. ǧ�ﶥ��[��] ����������\r\n","adj. �۵�\r\n","vt. ���ӣ����ѣ�̧����ǧ�ﶥ����ĳ��\r\n"],"type":1}}
    translate_results = translate_results['translateResult'][0][0]['tgt']
    #��ӡ������Ϣ
    print("����Ľ���ǣ�%s"%translate_results)
