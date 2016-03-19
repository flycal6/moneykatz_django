"""
Django settings for moneykatz_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from secrets import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['moneykatz.com', 'www.moneykatz.com', 'www.drycountrybrewing.com', 'drycountrybrewing.com']

# Application definition

INSTALLED_APPS = (
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'moneykatz',
    'bootstrap3',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Set daily cron job of python manage.py clearsessions
SESSION_COOKIE_AGE = 1209600

ROOT_URLCONF = 'moneykatz_django.urls'

WSGI_APPLICATION = 'moneykatz_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'moneykatz_database',
        'USER': 'flycal6',
        'PASSWORD': 'Kernut1!',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/accounts/login/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = '/home/flycal6/webapps/static/'

STATIC_URL = 'http://moneykatz.com/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    '/home/flycal6/webapps/mkatzdjango/moneykatz_django/media/media/',
    '/home/flycal6/webapps/mkatzdjango/moneykatz_django/media/uploads',
)

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (TEMPLATE_PATH,
                 )

MEDIA_URL = 'http://moneykatz.com/media/'

MEDIA_ROOT = '/home/flycal6/webapps/media/'

# Registration Redux

REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/moneykatz/'
LOGIN_URL = '/accounts/login/'

# Filebrowser Settings

from filebrowser.settings import settings
FILEBROWSER_DIRECTORY = getattr(settings, 'FILEBROWSER_DIRECTORY', MEDIA_ROOT)

# Email Settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # change to console.EmailBackend for testing
DEFAULT_FROM_EMAIL = website_email
EMAIL_HOST = email_host
EMAIL_HOST_USER = host_user
EMAIL_HOST_PASSWORD = host_password
EMAIL_USE_TLS = True
EMAIL_PORT = port

ADMINS = (admin1, admin2, admin3)
SERVER_EMAIL = admin1
