# -*- encoding: utf-8 -*-
"""
 ENVIRONMENT VARIABLES PYCHARM:
 DB_NAME
 DB_HOST
 DB_USER
 DB_PASSWORD
 WKHTMLTOPDF
 FILE_SETTINGS
"""
from .settings import *
import json
import os

NAME = os.environ.get('NAME_BD')
USER = os.environ.get('USER_BD')
PASSWORD = os.environ.get('PASSWORD_BD')
HOST = os.environ.get('HOST_BD')

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': 3306
    }
}

