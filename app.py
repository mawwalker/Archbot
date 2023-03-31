from flask import Flask
from flask import request
from flask import Response
from tgbot import TG
import json

app = Flask(__name__)
with open('config/config.json', 'r') as f:
    data = json.loads(f.read())
config = data

@app.route(f"/{config['access_token']}", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        tg_bot = TG()
        tg_bot.parse_message(msg)
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(debug=True)
