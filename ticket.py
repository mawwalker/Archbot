import requests
from requests.exceptions import RequestException
import sys
import json


class Ticket():
    def __init__(self, fs, ts, date, train_type):
        # 构造url请求的基本参数
        # 模拟浏览器的头部
        self.headers = {'content-type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/75.0.3770.100 Safari/537.36'}
        self.columns = ['车次', '出发时间', '到达时间', '历时', '商务座',
                        '特等座', '一等', '二等', '高级软卧', '软卧', '硬卧',
                        '软座', '硬座', '无座', '其他']

        # 本地存放了站点的json文件，通过get_stations.py获取，需要定时更新
        try:
            with open('/stations/stations.json', encoding='utf-8') as cf:
                stations = json.load(cf)
                start_val = stations[fs]
                dest_val = stations[ts]
        except Exception:
            start_val = self.get_station(fs)
            dest_val = self.get_station(ts)
        self.train_type = train_type
        # date = self.str_to_time(date)
        # 查询车票的url, 12306API
        self.url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date, start_val, dest_val)

    def get_station(self, station_name):
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                dict_data = {}
                text = response.text
                str_split = text.split('@')
                for chars in str_split[1:]:
                    station = chars.split('|')
                    dict_data[station[1]] = station[2]
                return dict_data[station_name]
        except RequestException:
            print("ERROR: unable to get station value")
            return 'ERROR'

    def get_ticket(self):
        trains = []
        requests.packages.urllib3.disable_warnings()
        html = requests.get(self.url, headers=self.headers, verify=False)
        self.available_trains = html.json()['data']['result']
        for item in self.available_trains:
            cm = item.split('|')
            train_no = cm[3]
            if (train_no[0] == self.train_type) or (self.train_type == ''):
                train = [
                    train_no,
                    cm[8],
                    cm[9],
                    cm[10],
                    cm[32],
                    cm[25],
                    cm[31],
                    cm[30],
                    cm[21],
                    cm[23],
                    cm[28],
                    cm[24],
                    cm[29],
                    cm[26],
                    cm[22]]
                trains.append(train)
            # self.pt.add_row(train)
            print(train)
        # print(self.pt)
        return trains


def main():
    # 获取系统传入的参数，运行：python 12306_API.py 北京 上海 2019-07-01
    sys_argv = sys.argv
    fs = sys_argv[1]
    ts = sys_argv[2]
    date = sys_argv[3]
    if len(sys_argv) == 5:
        train_type = sys_argv[4]
    else:
        train_type = ''
    # 创建查询火车票的对象
    tk = Ticket(fs, ts, date, train_type)
    tk.get_ticket()


if __name__ == '__main__':
    main()
    print('程序运行结束')
    print('############################################################')
    print('############################################################')
    print('############################################################')
    print('############################################################')
