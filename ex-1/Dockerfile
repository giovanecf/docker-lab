FROM python:latest

WORKDIR /usr/src/

ENV FLASK_APP=app.py

COPY ./assets/* .

RUN pip install -r requirements.txt

CMD ["flask","run","--host=0.0.0.0"]
