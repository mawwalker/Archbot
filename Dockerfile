FROM tiangolo/uwsgi-nginx-flask
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
