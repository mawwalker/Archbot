#!/usr/bin/python
# coding=utf-8
from google.cloud import translate
# from google.cloud import storage
import os


class google_translate():
    def __init__(self, input_text):
        self.input_text = input_text
        # 定义翻译程序
        self.translate_client = translate.Client()

    def get_target(self):
        # 获取输入文本的信息，便于识别语言
        target = self.translate_client.detect_language(self.input_text)
        # 实现中英互译
        if target["language"] == 'en':
            self.target_lan = 'zh-CN'
        elif target["language"] == 'zh-CN':
            self.target_lan = 'en'

    def c_e_translate(self):
        self.get_target()
        # 将输入文本进行翻译，自动识别中英文，互译
        translation = self.translate_client.translate(
            self.input_text,
            target_language=self.target_lan)
        # print(u'Text: {}'.format(self.input_text))
        # print(u'Translation: {}'.format(translation['translatedText']))
        return translation['translatedText']


if __name__ == '__main__':
    # 引入谷歌身份密钥文件
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'config/service_account.json'
    text = input('请输入需要翻译的内容：')
    trans = google_translate(text)
    translation = trans.c_e_translate()
    print(translation)
