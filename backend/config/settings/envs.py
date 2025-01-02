import environ

env = environ.Env()
env.read_env()

# --- Django ---
# ------------------------------------------------------------------------------
SECRET_KEY = env.str('SECRET_KEY', '59ffe99291f6d73ddefc823b658a89eab17a9dbd7da20c457b')

# --- Database ---
# ------------------------------------------------------------------------------
DB_HOST = env.str('DB_HOST')
DB_NAME = env.str('DB_NAME')
DB_USER = env.str('DB_USER')
DB_PASSWORD = env.str('DB_PASS')
