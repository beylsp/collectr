#!/bin/bash
gunicorn app:app --daemon
python collectr/crawler/worker.py
