import os

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-me"
    )

    SQLALCHEMY_DATABASE_URI = \
        "sqlite:///cybersentinel.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
