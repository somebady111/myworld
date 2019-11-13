# /usr/bin/python3
# coding='utf-8'
from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myworld',
        'USER':'root',
        'PASSWORD':'jing19961219',
        'HOST':'localhost',
        'PORT':3306,
        'CONN_MAX_AGE':5*60,
        'OPTIONS':{'charset':'utf8mb4'}
    }
}