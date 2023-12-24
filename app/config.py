import os

from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

class DevelopementConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False