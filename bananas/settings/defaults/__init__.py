from os.path import abspath, dirname, join

from setup_warnings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'chris@chris-lamb.co.uk'
DEFAULT_FROM_EMAIL = SERVER_EMAIL

ADMINS = (
)

INTERNAL_IPS = (
    '127.0.0.1',
)

BANANAS_BASE = dirname(dirname(dirname(dirname(abspath(__file__)))))

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bananas',
        'USER': 'bananas',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '6432',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

APPEND_SLASH = False

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')zh7swqp8%)__-x4i=_+olfr*@28oq@u!rk__5maw@_sdzb^gj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django_keyerror.middleware.KeyErrorMiddleware',
    'bananas.utils.middleware.TransactionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'cache_toolbox.middleware.CacheBackedAuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_autologin.middleware.AutomaticLoginMiddleware',
)

ROOT_URLCONF = 'bananas.urls'

TEMPLATE_DIRS = (
    join(BANANAS_BASE, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.sessions',

    'debug_toolbar',
    'django_autologin',
    'django_extensions',
    'django_keyerror',
    'django_yadt',
    'email_from_template',
    'south',

    'bananas.reviews',
    'bananas.reviews.reviews_admin',
    'bananas.debug',
    'bananas.utils',
    'bananas.static',
)

INTERNAL_IPS=(('127.0.0.1',))

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'bananas',
    }
}

SECRET_KEY = ')7h7swqp8%)__-x9i=_+olfr*@28oq@u!rk__5maw@_sdzb^gj'

# fcgi is really broken
FORCE_SCRIPT_NAME = ''

SITE_URL = 'https://chris-lamb.co.uk'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_DEFAULT_ACL = 'public-read'
AWS_ACCESS_KEY_ID = 'AKIAJ2MH6KAU3WOSKPCQ'
AWS_S3_CUSTOM_DOMAIN = 'd1icoid1cnixnp.cloudfront.net'
AWS_QUERYSTRING_AUTH = False
AWS_SECRET_ACCESS_KEY = 'PFc5/5lERCkf3uNj+Icyx0PHe9ZrHcdemw/Y1kqr'
AWS_STORAGE_BUCKET_NAME = 'bananas'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

LOGIN_URL = '/admin/login' # bananas:reviews:admin:login

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.csrf',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'bananas.debug.context_processors.settings_context',
)

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_AGE = 86400 * 365 * 10
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

STATIC_MEDIA_URL = '//d3iu69lz2dsmya.cloudfront.net/media/%(hash).6s/%(path)s'
STATIC_MEDIA_ROOT = join(BANANAS_BASE, 'media')

DATABASE_ENGINE = None # for debug toolbar

LOGIN_REDIRECT_URL = '/admin'

AKISMET_KEY = '9ec6f3a8761a'

KEYERROR_SECRET_KEY = '3927184f06989f054a5aa35c7bbf3f9b7ab2c268'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

SOUTH_TESTS_MIGRATE = False

FONTS_ENABLED = True
