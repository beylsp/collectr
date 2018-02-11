import os

from os.path import abspath, dirname, join

curdir = abspath(dirname(__file__))


class Config(object):
    ENTRIES_PER_PAGE = 60


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(Config):
    pass


class DevelopmentConfig(Config):
    curdir = abspath(dirname(__file__))
    dbfile = join(dirname(curdir), 'db', 'data', 'dev.sqlite.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % dbfile


config = {
    'production': ProductionConfig,
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
