＃！/ usr / bin / env python
＃ -  *  - 编码：utf-8  -  *  -
从 HTMLParser 导入 HTMLParser
导入 urllib2
进口 json
导入系统
从 xml.etree 导入 ElementTree 作为 ET
从 urllib 导入 urlencode，urlopen

＃ Python2.5初始化后会删除sys.setdefaultencoding这个方法，我们需要重新载入
重新加载（sys）
sys.setdefaultencoding（' utf-8 '）


 HandleHtml 类（HTMLParser）：
    def  __init__（self）：
        self .data = []
        self .is_find =  False
        self .zhanghao =  ' '
        HTMLParser的。__init__（自）

    def  handle_starttag（self，tag，attrs）：
        如果 tag ==  ' font '：
            对于名称，值在 ATTRS：
                如果 name ==  ' size ' 和 value ==  ' 4 '：
                    self .is_find =  True

    def  handle_data（self，data）：
        如果 self .is_find 而 不是（data.find（'（'）> =  0  和 data.find（'）'）> =  0  或 data.find（u '点击查看'）> =  0）
            self .zhanghao =数据

    def  handle_endtag（self，tag）：
        如果 tag ==  ' font '：
            如果 自己。张豪和 len（self .zhanghao.strip（））：
                self .data.append（self .zhanghao）
            self .zhanghao =  ' '
            self .is_find =  False

    def  get_result（self）：
        返回 自我数据


def  find_zhanghao_url（）：
    request = urllib2.Request（' http://www.521xunlei.com/ '）
    result = urllib2.urlopen（request）.read（）。decode（' gbk '）
    str_index = result.find（û '爱密码迅雷共享'）
    first_href_index = result.find（' href '，str_index）
    second_href_index = result.find（' href '，first_href_index）
    URL =  ' http://www.521xunlei.com/ '  +导致[second_href_index + 6：second_href_index + 26 ]
    返回 url


def  get_all_zhanghao（内容）：
    parser = HandleHtml（）
    parser.feed（内容）
    all_zhanghao = parser.get_result（）

    返回 all_zhanghao


def  get_xlhy（）：
    url = find_zhanghao_url（）
    request = urllib2.Request（url）
    content = urllib2.urlopen（request）.read（）。decode（' gbk '）
    all_zhanghao = get_all_zhanghao（content）

    items = []
    为 zhanghao 在 all_zhanghao：
        title = zhanghao
        arg = zhanghao
        items.append（{
            ' uid '：zhanghao，
            '标题'：标题，
            ' arg '：arg，
            ' description '：zhanghao，
            ' icon '： ' icon.jpg '，
        }）
    xml = generate_xml（items）
    返回 xml


def  generate_xml（items）：
    xml_items =  ET .Element（' items '）
    对于项目中的项目：
        xml_item =  ET .SubElement（xml_items，' item '）
        对于关键的 item.keys（）：
            如果关键的（“ ARG ”）：
                xml_item.set（key，item [key]）
            否则：
                child =  ET .SubElement（xml_item，key）
                child.text = item [key]
    返回 ET .tostring（xml_items）

如果 __name__  ==  ' __main__ '：
    打印 get_xlhy（）