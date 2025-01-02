from config.settings.common import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ['*']

# SWAGGER
# ------------------------------------------------------------------------------
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {'apiKey': {'type': 'apiKey', 'name': 'Token', 'in': 'header'}},
    'SHOW_REQUEST_HEADERS': True,
    'JSON_EDITOR': True,
    'LOGIN_URL': 'admin:login',
    'LOGOUT_URL': 'admin:logout',
    'OPERATIONS_SORTER': 'alpha',
}
