# -*- coding: utf-8 -*-
from qqbot import QQBotSlot as qqbotslot, RunBot

@qqbotslot
def onQQMessage(bot, contact, member, content):
	if '@Me' in content:
		# pass
    # if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人123')
    elif content == '-stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

if __name__ == '__main__':
    RunBot()