from flask import Flask
from opbeat.contrib.flask import Opbeat

app = Flask(__name__)
opbeat = Opbeat(
    app,
    organization_id='c6b1b6f06dab409db01224faa85c9887',
    app_id='209b15af04',
    secret_token='b5b3969552cbaf97b75e94014bff7108d8c0be6b'
)

from collectr import views  # noqa
