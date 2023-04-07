# here's a sample code for a config.py file that can be used to store the 
# configuration settings for your Google Transit project
# In this example, we have a base Config class that defines the common settings 
# for all environments. 
# Then we define a DevelopmentConfig and a ProductionConfig class that inherit from Config 
# and set environment-specific values.
# In this case, we have set DEBUG to True in the DevelopmentConfig class, 
# and we have set the SQLALCHEMY_DATABASE_URI and SECRET_KEY values 
# for both DevelopmentConfig and ProductionConfig.

import os

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SECRET_KEY = 'my_secret_key'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
