import os
import logging

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    logging.info('Python web app test')
    return os.environ['hello']