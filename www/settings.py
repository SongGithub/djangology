"""
Django settings for djangology project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

IS_HEROKU = False
if os.getenv('DATABASE_URL', None) is not None:
    IS_HEROKU = True

TEMPLATE_DIRS = [
    os.path.join(os.path.dirname(__file__),'templates'),
]
#here is where to paste static files to
STATIC_ROOT = (
    os.path.join(os.path.dirname(__file__), "static","staticonly")
    
)
STATIC_URL = '/static/'
#it is where to look for static files
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), "static"),
    # os.path.join(os.path.dirname(__file__), '/www/static/'),
    
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8unzs1zdbq&n-tfo8cex%(dw5+fj!&%qzwd8l-o*qfrhq#s#&'

DEBUG = not IS_HEROKU 
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = "*"


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions', 
    'south',
    # 'www',
    'www.apps.todo',
    'rest_framework',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
    'FILTER_BACKEND' : 'rest_framework.filters.DjangoFilterBackend',
}
ROOT_URLCONF = 'www.urls'

WSGI_APPLICATION = 'www.wsgi.application'

##legacy database settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'djangology',
#         'USER':'dev_app',
#         'PASSWORD':'legend',
#         'HOST':'localhost',
#         'PORT':'5433',

#     }
# }

'''switch between Heroku server and local regarding db settings '''
if IS_HEROKU:
    # On Heroku
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    # Local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'djangology',
            'USER':'dev_app',
            'PASSWORD':'legend',
            'HOST':'localhost',
            'PORT':'5433',
        }
    }

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    # 'DEFAULT_MODEL_SERIALIZER_CLASS':
    #     'rest_framework.serializers.HyperlinkedModelSerializer',

    # # Use Django's standard `django.contrib.auth` permissions,
    # # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = False

USE_L10N = True

USE_TZ = True
