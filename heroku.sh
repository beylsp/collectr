#!/bin/bash
gunicorn --log-level debug --bind 0.0.0.0:$PORT collectr.web.wsgi:app --daemon
python collectr/service/worker.py
