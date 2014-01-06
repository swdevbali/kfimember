"""
Django settings for kfimember project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
ON_OPENSHIFT = False
if os.environ.get('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'igs_-75&c!j*997%p*^6kw=i$!r2nikkche&_vj%3@w#+nx35t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'kfimemberapp',
	'south'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kfimember.urls'

WSGI_APPLICATION = 'kfimember.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if ON_OPENSHIFT:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
			'NAME': 'kfimember',  # Or path to database file if using sqlite3.
			'USER': '',
			'PASSWORD': '',
			'HOST': os.environ.get('$OPENSHIFT_POSTGRESQL_DB_HOST',''),                      # Set to empty string for localhost. Not used with sqlite3.
			'PORT': os.environ.get('$OPENSHIFT_POSTGRESQL_DB_PORT',''),                      # Set to empty string for default. Not used with sqlite3.
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2', #'django.db.backends.sqlite3',
			'NAME': 'kfimember', #os.path.join(BASE_DIR, 'db.sqlite3'),
			'USER' : 'postgres',
			'PASSWORD' : '',
			'HOST' : 'localhost',
			'PORT' : ''
		}
	}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '../static'