from .base import *

SECRET_KEY = 'secured0xb8$c!5xcdf(s56m800f(g1wi3qs5rg&to9dio)xtos&6s1j3'

DEBUG = False

ALLOWED_HOSTS = [
    'http://127.0.0.1:8000/'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}