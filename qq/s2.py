# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
    if '@ME' in content:
    # if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
