#!/bin/bash
# . venv/bin/activate && uwsgi --socket 172.17.0.1:8000 -p -w app:app
app="tgbot"
docker build -t ${app} .
docker run -d \
  --name=${app} \
  -v $PWD:/app ${app}