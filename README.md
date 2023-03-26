# Archbot
A simple telegram bot using flask webhook.

## setWebhook
open your browser, then open this url:
```
https://api.telegram.org/bot{bottoken}/setWebhook?url=https://yourdomain.com
```
change {bottoken} to your bot api token, then url to your domain.

For example, if your bottoken is 111111111:aaaaaaaaaaaaaaaaaaaa, and you domain is https://example.com/tgaaaaaaa.
You should go to the following url:
```
https://api.telegram.org/bot111111111:aaaaaaaaaaaaaaaaaaaa/setWebhook?url=https://example.com/tgaaaaaaa
```
**Attention: There is always a `bot` word before your token. Besides, Strongly recommend that you set up your webhook to be COMPLEX, such as adding a token after the domain name.**

## config
```
cp config/config.example.json config/config.json
```
Then change access_token to your telegram bot api token.
webhook_url to your bot wehook url.
like:
```
{
    "access_token":"111111111:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "webhook_url":"https://youdomain.com/"
}
```

## Deploy
### Docker run
```
./start.sh
```
### Docker Compose
for docker compose >= v2:
```
docker compose up -d
```
for docker compose < v2:
```
docker-compose up -d
```
## nginx proxy
logging to your nginx-proxy-manager, add a proxy to tgbot:80

You can refer to this blog for more details:

<https://smartdeng.com/2019/06/24/flask_python-telegram-bot/>

