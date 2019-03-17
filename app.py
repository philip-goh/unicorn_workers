import eventlet
# Comment this out to disable eventlet monkey patching. This will mean that the
# `sleep` function is synchronous and will block.
eventlet.monkey_patch()
from flask import Flask
import time
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")


app = Flask(__name__)
counter = 0

@app.route("/")
def do_something():
    global counter
    counter += 1
    req_num = counter
    logging.info(f"Initiating request: {req_num}")
    time.sleep(5)
    logging.info(f"Completing request: {req_num}")
    return "OK"
