#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import request
import os
import json
from tgbot import TG

# 导入谷歌翻译的身份验证文件
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config/service_account.json'


app = Flask(__name__)

with open('config/config.json', encoding='utf-8') as cf:
    config = json.load(cf)
access_token = config["access_token"]


@app.route("/{}".format(access_token), methods=["POST", "GET"])
def archbot():
    if (request.method == "POST") or (request.method == "GET"):
        tg_bot = TG()
        text = tg_bot.bot_main()
    else:
        text = 'ERROR'
    return text


if __name__ == '__main__':
    app.run()
