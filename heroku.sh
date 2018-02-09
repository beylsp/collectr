#!/bin/bash
gunicorn collectr:app --daemon
python collectr/crawler/worker.py
