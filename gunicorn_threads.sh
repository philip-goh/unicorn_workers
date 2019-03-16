#!/bin/bash

gunicorn -w 1 --threads 10 -b 127.0.0.1:5000 app:app
