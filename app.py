import eventlet
# Comment this out to disable eventlet monkey patching. This will mean that the
# `sleep` function is synchronous and will block.
# eventlet.monkey_patch()
from flask import Flask
import time
import logging
import math

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")


app = Flask(__name__)
counter = 0
cpu_counter = 0

@app.route("/")
def do_something():
    global counter
    counter += 1
    req_num = counter
    logging.info(f"Initiating request: {req_num}")
    time.sleep(5)
    logging.info(f"Completing request: {req_num}")
    return "OK"


def intensive_cpu():
    # Calculate square root 1000 times
    for i in range(1000000):
        x = math.sqrt(0.9) * math.sqrt(0.9)
    return x

@app.route("/cpu_bound")
def do_something_cpu_bound():
    global cpu_counter
    cpu_counter += 1
    req_num = cpu_counter
    logging.info(f"Initiating CPU bound request: {req_num}")
    intensive_cpu()
    logging.info(f"Completing CPU bound request: {req_num}")
    return "OK"
