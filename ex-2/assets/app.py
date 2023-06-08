import logging
from flask import Flask, request
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

handler = RotatingFileHandler('/tmp/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


@app.route("/")
def hello_world():
    app.logger.error(('The referrer was {}'.format(request.referrer)))
    return "<p>Hello, World!</p>"
