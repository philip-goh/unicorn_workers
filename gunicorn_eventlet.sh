#!/bin/bash

gunicorn -w 1 -k eventlet -b 127.0.0.1:5000 app:app
