import os

class Development(object):
    """
    Development environment configuration
    """

    DEBUG = True
    TESTING = False
    SECRET_KEY = "6KXjtFqhwdPn-qJOFOdKSsPKa-Xv9EWUSwYSvLzKCgk="
    SESSION_COOKIE_SECURE = False


class Production(object):
    """
    Production environment configurations
    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    SESSION_COOKIE_SECURE = True


app_config = {
    "development": Development,
    "production": Production,
}
