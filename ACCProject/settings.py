'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


"""
Django settings for ACCProject project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!vc3_zj)yp4fke24wan1289ap5)69t4fd@(el#uu(%a95tkd^!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0868f06d1e21.ngrok.io','127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_json_api',
    'SocialBookApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ACCProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ACCProject.wsgi.application'

FERNET_KEYS = [
    "q^@n3ybwz%_w+4pqk_%rhz#_^vks-l^!&4)&-&+==ioag&lj5e"
]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'ProjectDB',

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LOGGING_CONFIG = None

LOGGING = {

    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        }
    },

    'handlers': {
            'task': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': str(BASE_DIR) + '/logs/task.log',
                'formatter': 'verbose',
                'maxBytes': 5000000,
                'backupCount' : 2
            },
            'request': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': str(BASE_DIR) + '/logs/debug.log',
                'formatter': 'verbose',
                'maxBytes': 5000000,
                'backupCount' : 2
            },
            'system': {
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': str(BASE_DIR) + '/logs/system.log',
                'formatter': 'verbose',
                'maxBytes': 5000000,
                'backupCount': 2
            },

        },

    'loggers': {

            'django': {
                'handlers': ['system'],
                'propagate': True,
            },

            'book.request': {
                'level': 'DEBUG',
                'handlers': ['request'],
                'propagate': True,
            },

            'book.task': {
                'level': 'DEBUG',
                'handlers': ['task'],
                'propagate': True,
            },


    }
}

import logging.config
logging.config.dictConfig(LOGGING)

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'