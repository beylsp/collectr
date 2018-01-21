import helper
import os
from flask import Flask
from flask import g
from werkzeug.utils import find_modules
from werkzeug.utils import import_string
from collectr.blueprints.collectr import init_db


def create_app(config=None):
    app = Flask('collectr')

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'collectr.db'),
        ENTRIES_PER_PAGE=30,
    ))
    app.config.update(config or {})
    app.config.from_envvar('COLLECTR_SETTINGS', silent=True)

    app.add_template_filter(helper.pluralize)

    register_blueprints(app)
    register_cli(app)
    register_teardowns(app)

    return app


def register_blueprints(app):
    for name in find_modules('collectr.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
        return None


def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        init_db()
        print('Initialized the database.')


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
