from flask import Flask
from opbeat.contrib.flask import Opbeat
from config import config

opbeat = Opbeat()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    if not app.testing:
        opbeat.init_app(app)
    return app

from collectr import views  # noqa
