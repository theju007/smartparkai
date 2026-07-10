import os


class Config:

    SECRET_KEY = "smartpark-secret-key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost/smart_parking"

    SQLALCHEMY_TRACK_MODIFICATIONS = False