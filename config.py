import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_key_123"

    MONGODB_SETTINGS = { 'db': 'Course_Enrollment'}
