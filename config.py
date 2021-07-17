import os


class BaseConfig(object):
    DEBUG = True
    DEVELOPMENT = True


class ProductionConfig(BaseConfig):
    DEVELOPMENT = False
    DEBUG = False
