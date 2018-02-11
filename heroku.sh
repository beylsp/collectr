#!/bin/bash
gunicorn --bind 0.0.0.0:$PORT collectr.web.wsgi:app --daemon
python collectr/service/worker.py
