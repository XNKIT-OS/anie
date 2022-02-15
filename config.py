import os

class Config(object):
    APP_ID = os.environ.get("APP_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    # Pyrogram Session
    ANIE_SESSION = os.environ.get("ANIE_SESSION", "")
    CMD_PREFIX = os.environ.get("CMD_PREFIX", ".")
    MONGODB_URL = os.environ.get("MONGODB_URL")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
