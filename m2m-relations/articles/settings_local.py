import os
from .settings import BASE_DIR

SECRET_KEY = 'd+mw&f33mscg5i&tx+#@bf+6m%e+d5z!u#!n%z-^o9u7y1felv2o&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'netology_m2m_2',
        'USER': 'postgres',
        'PASSWORD': 'zxcvbn123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}