"""The application module, containing the application factory function."""
from flask import Flask
from opbeat.contrib.flask import Opbeat
from config import config
from collectr.views.products import products

opbeat = Opbeat()


def create_app(config_name):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration to use.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(products)

    if not app.testing:
        opbeat.init_app(app)
    return app
