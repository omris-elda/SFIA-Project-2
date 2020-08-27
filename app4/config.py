import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev" # remember to remove 'dev' before production
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "mysql+pymysql://root:root@34.89.28.17:3306/project2db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False