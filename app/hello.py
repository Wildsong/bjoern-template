import sys
from flask import Flask
import logging
from requestlogger import WSGILogger
from datetime import datetime as dt

app = Flask(__name__)
counter = 0

def MyFormatter():
    return Formatters.my_format
class Formatters(object):
    @staticmethod
    def my_format(status_code, environ, content_length, **kwargs):
        now = dt.now()
        try:
            referer = environ['HTTP_REFERER']
        except KeyError:
            referer = 'None'
        return f"{now} {status_code} {referer} {environ['PATH_INFO']}"

@app.route("/")
def hello_world():
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    message = f"Bjoern serving Flask WSGI Python {version} in a Docker container"
    return message.encode("utf-8")

@app.route("/status")
def status():
    global counter
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    message = f"<h1>Status</h1> {version} {counter}"
    counter += 1
    return message.encode("utf-8")

handlers = [ logging.StreamHandler(), ]
application = WSGILogger(app, handlers, MyFormatter())

print("Hello app running. http://localhost:12345/")

