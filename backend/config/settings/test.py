from config.settings.dev import *  # noqa

DEBUG = False

TEST_RUNNER = 'common.test.CustomTestRunner'
SECRET_KEY = '59ffe99291f6d73ddefc823b658a89eab17a9dbd7da20c457b'

PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
