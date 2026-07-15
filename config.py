import os


class Config:

    SECRET_KEY = "smartpark-secret-key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost/smart_parking"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RAZORPAY_KEY_ID = "rzp_test_TDoQQFkUZDVF9U"

    RAZORPAY_KEY_SECRET = "p68Ez9pRRIkEXcjCuWK1b7yr"