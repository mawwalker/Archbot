# Archbot
一个telegram机器人

### 文件说明

python3 配置需求在requirements.txt文件中

ticket.py 为12306查询火车票余票的文件目前该机器人的功能：

### 使用

config.json文件中access_token 修改为自己telegram-bot的token

设置webhook为: 

```bash
https://yourdomain.com/{yourtoken}
```

其中yourdomain.com 改成自己的域名，yourtoken 改为自己的机器人token

配置成功后对机器人发消息即可：



/help 查看帮助

/12306 北京 上海 20191001 查询2019年10月01日从北京到上海所有火车票

/12306 北京 上海 20191001 G 只显示高铁



具体的配置过程可参考我的博客：

<https://smartdeng.com/2019/06/24/flask_python-telegram-bot/>

