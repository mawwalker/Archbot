#!/usr/bin/env python
# coding=utf-8
import json
from flask import request
import requests


class TG():
    def __init__(self):
        with open('config/config.json', encoding='utf-8') as cf:
            config = json.load(cf)
        self.access_token = config["access_token"]

    def help(self, chat_id, msg):
        self.tel_send_message(chat_id=chat_id, text="/help 查看帮助\n")

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
            
    def parse_message(self, message):
        print("message-->",message)
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
        if "/help" in txt:
            self.help(chat_id, txt)
        else:
            text = 'Hello'
            self.tel_send_message(chat_id=chat_id, text=text)
 
    def tel_send_message(self, chat_id, text):
        url = f'https://api.telegram.org/bot{self.access_token}/sendMessage'
        payload = {
                    'chat_id': chat_id,
                    'text': text
                    }
    
        r = requests.post(url,json=payload)
        return r
