#!/usr/bin/env python
# coding=utf-8
import json
from flask import request
import requests
from src.gemini import process_gemini


class TG():
    def __init__(self):
        with open('config/config.json', encoding='utf-8') as cf:
            config = json.load(cf)
        self.access_token = config["access_token"]
        self.translate_command = ["english", "chinese", "spanish", "french", 
                                  "german", "hindi", "arabic", "japanese", "korean",
                                  "russian"]

    def help(self, chat_id, msg):
        help_msg = f"""/help 查看帮助\n/<language> 将文字翻译成指定语言，示例：/chinese good morning. \n目前支持的语言列表: \nenglish, chinese, spanish, french, german, hindi, arabic, japanese, korean, russian.\n其他: 只要不以/开头，则会调用对话模型，进行对话，无上下文功能。
        """
        self.tel_send_message(chat_id=chat_id, text=help_msg)
    
    def translate(self, chat_id, input_msg, translate_type):
        prompt = f"translate the text to {translate_type}: {input_msg}"
        result = process_gemini(prompt)
        self.tel_send_message(chat_id=chat_id, text=result)
            
    def parse_message(self, message):
        print("message-->",message)
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        if not txt.startswith('/'):
            # 如果不是命令开头，则使用对话
            result = process_gemini(txt)
            self.tel_send_message(chat_id=chat_id, text=result)
            return
        
        txt_split = txt.split(" ")
        command = txt_split[0][1:]
        user_text = ' '.join(txt_split[1:])
        if command == 'help':
            self.help(chat_id, txt)
        elif command.lower() in self.translate_command:
            if len(user_text) == 0:
                self.tel_send_message(chat_id=chat_id, text="Input Text empty")
                return
            self.translate(chat_id=chat_id, input_msg=user_text, translate_type=command)
        else:
            text = 'Unknow Command, Use /help to check support commands.'
            self.tel_send_message(chat_id=chat_id, text=text)
 
    def tel_send_message(self, chat_id, text):
        url = f'https://api.telegram.org/bot{self.access_token}/sendMessage'
        payload = {
                    'chat_id': chat_id,
                    'text': text
                    }
    
        r = requests.post(url,json=payload)
        return r
