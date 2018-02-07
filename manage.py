#!/usr/bin/env python
"""Management script."""
import os
from flask_script import Manager
from collectr.factory import create_app

if os.path.exists('.env'):
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
