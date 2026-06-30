import os

class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change_this_secret_key"
    )

    SQLALCHEMY_DATABASE_URI = "sqlite:///cybersentinel.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
