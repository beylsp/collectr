"""Application configuration module."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Parent configuration."""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuraton."""
    DEBUG = True


class TestingConfig(Config):
    """Test configuration."""
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
