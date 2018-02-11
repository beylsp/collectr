from flask import Flask
from werkzeug.utils import find_modules
from werkzeug.utils import import_string

from collectr.web import settings
from collectr.web.filters.words import pluralize


def create_app(config_name):
    """An application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.

    Args:
      config_name: string, the configuration to use.

    Returns:
      The application object.
    """
    app = Flask('collectr',
                template_folder='web/templates',
                static_folder='web/static')
    app.config.from_object(settings.config[config_name])

    app.add_template_filter(pluralize)

    register_blueprints(app)

    return app


def register_blueprints(app):
    for name in find_modules('collectr.web.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
        return None
