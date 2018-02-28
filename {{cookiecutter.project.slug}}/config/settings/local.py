# -*- coding: utf-8 -*-
"""
Local settings
- Run in Debug mode
- Use console backend for emails
"""

from .common import *  # noqa


# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
if 'TEMPLATES' in locals():
    for num,t in enumerate(TEMPLATES):
        if type(t.get('OPTIONS')) is dict:
            TEMPLATES[num]['OPTIONS']['debug'] = DEBUG


# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env(
    'DJANGO_EMAIL_BACKEND',
    default='django.core.mail.backends.console.EmailBackend'
)


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])

