# -*- coding: utf-8 -*-

from qqbot import QQBotSlot as qqbotslot, RunBot
import requests
KEY='70a315f07d324b3ea02cf21d13796605'
def answerQ(question):
    apiUrl='http://www.tuling123.com/openapi/api'
    print apiUrl
    data={'key':KEY,'info':question,'userid':'qq'}
    # try:
    payload = {'key':KEY,'info':question}
    r = requests.post(apiUrl, data=payload)      
    return r.text
    # except Exception as e:
        # return

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if '@ME' in content:
        bot.SendTo(contact, answerQ(content))
    # if content == '-hello':
    #     bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == '__main__':
    # 注意： 这一行之前的代码会被执行两边
    # 进入 RunBot() 后，会重启一次程序（ subprocess.call(sys.argv + [...]) ）
    RunBot()
    # 注意: 这一行之后的代码永远都不会被执行。
