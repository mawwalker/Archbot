#!/usr/bin/python
# coding=utf-8
import json
import requests

def station_name():
    image_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
    r = requests.get(image_url)
    with open("station_name.js", 'wb') as f:
        f.write(r.content)

    f = open('station_name.js', 'r')
    # print(f)
    line = f.readline()
    # print(line)
    station_list = line.split("'")[1].split('|')
    stations = []
    station_dict = {}
    for i in range(0, len(station_list) - 1, 5):
        tmp = []
        for j in range(5):
            tmp.append(station_list[i + j])
        stations.append(tmp)
        station_dict[tmp[1]] = tmp[2]

    with open("stations.json", "w") as f:
        json.dump(station_dict, f, ensure_ascii=False, indent=4)
        print("加载入文件完成...")


if __name__ == '__main__':
    station_name()
