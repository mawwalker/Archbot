#!/usr/bin/env python
# coding=utf-8
import json
from flask import request
import telegram
# from telegram.ext import Updater
# from telegram.ext import CommandHandler
import logging
# from telegram.ext import MessageHandler, Filters
from ticket import Ticket
from tlbot import tuling
# from telegram import InlineQueryResultArticle, InputTextMessageContent
# from telegram.ext import InlineQueryHandler


class TG():
    def __init__(self):
        with open('config.json', encoding='utf-8') as cf:
            config = json.load(cf)
        self.access_token = config["access_token"]
        self.bot = telegram.Bot(token=self.access_token)

    def help(self, msg):
        self.bot.send_message(chat_id=msg.chat_id, text="/help 查看帮助\n\
/12306 北京 上海 2019-07-01 查询火车票余额，如果想查询特定类型车的，\
请输入 /12306 北京 上海 2019-07-01 G 表示只显示高铁")

    def echo(self, msg):
        self.bot.send_message(msg.chat_id, text=msg.text)

    def list2str(self, trains, tk):
        # 用来存放最终合成的消息列表
        text_list = []
        for train in trains:
            temp = []
            for i in range(15):
                # 当该列不为空时才合成
                if train[i] != '':
                    temp.append(tk.columns[i] + ":" + train[i])
            text_list.append(' | '.join(temp).upper())
        text_ticket = '\n\n'.join(text_list).upper()
        return text_ticket

    def q_ticket(self, msg):
        try:
            args = msg.text.split(' ')
            print(args)
            fs = args[1]
            ts = args[2]
            date = args[3]
            if len(args) == 5:
                train_type = args[4]
            else:
                train_type = ''
            # 创建火车票查询的对象
            tk = Ticket(fs, ts, date, train_type)
            # 获取所有查询到的车次信息
            trains = tk.get_ticket()
            # 将查询到的列表，转换成消息字符串
            text_ticket = self.list2str(trains, tk)
            self.bot.send_message(chat_id=msg.chat_id, text=text_ticket)
        except Exception:
            print("ERROR: something wrong!!!!")

    def bot_main(self):
        # 获取最新消息
        update = telegram.Update.de_json(request.get_json(force=True), self.bot)
        # print(update)
        if update is None:
            return "Show me your TOKEN please!"
        logging.info("Calling {}".format(update.message))
        self.handdle_message(update.message)
        return "ok"

    def handdle_message(self, msg):
        text = msg.text
        if "/12306" in text:
            self.q_ticket(msg)
        elif "/help" in text:
            self.help(msg)
        else:
            # 调用图灵机器人接口
            text_tuling = tuling(msg.text)
            self.bot.send_message(chat_id=msg.chat_id, text=text_tuling)
