# coding:utf-8
from qqbot import QQBotSlot as qqbotslot, RunBot
import requests
KEY='70a315f07d324b3ea02cf21d13796605'
def answerQ(question):
	apiUrl='http://www.tuling123.com/openapi/api'
	data={'key':KEY,'info':question,'userid':'qq'}
	try:
		r=requests.post(apiUrl,data=data).json()
		return r.get('text')
	except Exception as e:
		return

@qqbotslot
def onQQMessage(bot, contact, member, content):
    # if content == '-hello':
    if "@ME" in content:
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == '__main__':
    RunBot()