FROM python:3.10-slim

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD gunicorn --bind 0.0.0.0:8050 app.app:server