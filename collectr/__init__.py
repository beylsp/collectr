from flask import Flask

app = Flask(__name__)

from collectr import views  # noqa
