#!/usr/bin/env python
# coding=utf-8
import json
import urllib.request

def tuling(text_input):
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    req = {
        "perception":
        {
            "inputText":
            {
                "text": text_input
            },
            "selfInfo":
            {
                "location":
                {
                    "city": "上海",
                    "province": "上海",
                    "street": "文汇路"
                }
            }
        },
        "userInfo":
        {
            "apiKey": "08dd4d7baa4449beae52a4cab8f2e6c5",
            "userId": "OnlyUseAlphabet"
        }
    }
    # print(req)
    # 将字典格式的req编码为utf8
    req = json.dumps(req).encode('utf8')
    # print(req)
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    # print(response_str)
    response_dic = json.loads(response_str)
    # print(response_dic)
    intent_code = response_dic['intent']['code']
    results_text = response_dic['results'][0]['values']['text']
    print('Turing的回答：')
    print('code：' + str(intent_code))
    print('text：' + results_text)
    return results_text


if __name__ == '__main__':
    text_input = input('我：')
    tuling(text_input)
