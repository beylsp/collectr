import os

from os.path import dirname
from os.path import abspath
from os.path import join
from sqlalchemy import create_engine
from collectr.db.models import Base
from collectr.db.models import SparkModelData


path = os.getenv("DATABASE_URL", None)
if not path:
    curdir= abspath(dirname(__file__))
    dbfile = join(curdir, 'data', 'dev.sqlite.db')
    path = 'sqlite:///%s' % dbfile

engine = create_engine(path, echo=True)
Base.metadata.create_all(engine)
