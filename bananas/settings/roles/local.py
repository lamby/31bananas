from os.path import join, dirname, normpath

def base_dir(*paths):
    return join(
        dirname(dirname(dirname(dirname(normpath(__file__))))),
        *paths
    )

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bananas'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_URL = 'http://127.0.0.1:8000'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

MEDIA_URL = '/storage/'
MEDIA_ROOT = base_dir('storage')
STATIC_MEDIA_URL = '/media/%(path)s'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
