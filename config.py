import os


class BaseConfig(object):
    DEBUG = True
    DEVELOPMENT = True


class ProductionConfig(BaseConfig):
    DEVELOPMENT = False
    DEBUG = False
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION')
    AWS_SQS_QUEUE_URL = os.environ.get('AWS_SQS_QUEUE_URL')
    SENTRY_DSN = os.environ.get('SENTRY_DSN')
