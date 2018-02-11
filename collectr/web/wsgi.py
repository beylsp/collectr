import os

from collectr.web import factory


app = factory.create_app(os.getenv('CONFIG') or 'default')


if __name__ == '__main__':
    app.run()
