import json

with open('config/config.json', 'r') as f:
    data = json.loads(f.read())
config = data