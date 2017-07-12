from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['*']

# force https
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# AWS S3 settings
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

# AWS credentials
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# create a aws s3 bucket
AWS_AUTO_CREATE_BUCKET = True

# S3 URL
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Static Files
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'linuxluigi_com.s3_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# Media Files
MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'linuxluigi_com.s3_storages.MediaStorage'

"""
# For Using RDS DB
DATABASES = {    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'os.environ['DB_NAME']',
        'USER' : 'os.environ['DB_USER']r',
        'PASSWORD' : 'os.environ['DB_PASSWORD']',
        'HOST' : 'os.environ['DB_HOST']',
        'PORT' : 'os.environ['DB_PORT']',
    }
}
"""

""""
# Cloudflare
WAGTAILFRONTENDCACHE = {
    'cloudflare': {
        'BACKEND': 'wagtail.contrib.wagtailfrontendcache.backends.CloudflareBackend',
        'EMAIL': os.environ['CLOUDFLARE_EMAIL'],
        'TOKEN': os.environ['CLOUDFLARE_TOKEN'],
        'ZONEID': os.environ['CLOUDFLARE_ZONEID'],
    },
}
"""

# AWS ses for sending emails, need to be enabled first
# EMAIL_BACKEND = 'django_ses.SESBackend'
# AWS_SES_REGION_NAME = os.environ['AWS_SES_REGION_NAME']
# AWS_SES_REGION_ENDPOINT = os.environ['AWS_SES_REGION_ENDPOINT']

try:
    from .local import *
except ImportError:
    pass
