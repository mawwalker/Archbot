FROM tiangolo/uwsgi-nginx-flask
RUN apk --update add bash nano
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
