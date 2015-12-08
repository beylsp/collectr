from flask import Flask
from opbeat.contrib.flask import Opbeat
from config import config
from views.products import products

opbeat = Opbeat()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(products)

    if not app.testing:
        opbeat.init_app(app)
    return app
