#!/bin/bash
gunicorn --bind 0.0.0.0:$PORT collectr:app --daemon
python collectr/crawler/worker.py
