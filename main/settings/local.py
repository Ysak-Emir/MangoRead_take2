import os
import sys
from .base import *
from main.settings.base import BASE_DIR
from .base import MIDDLEWARE, TEMPLATES, AUTH_USER_MODEL, AUTH_PASSWORD_VALIDATORS
from .jazzmin import JAZZMIN_SETTINGS

JAZZMIN_SETTINGS["show_ui_builder"] = True
ALLOWED_HOSTS = ['*']
DEBUG = True if os.environ.get('DEBUG', 'off') == 'on' else False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME", "manga_db"),
        'PASSWORD': os.environ.get("DB_PASSWORD", "123456"),
        'USER': os.environ.get("DB_USER", "admin"),
        'HOST': os.environ.get("DB_HOST", "db"),
        'PORT': '5432'
    }
}

# Static assets
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ROOT_URLCONF = 'main.urls'