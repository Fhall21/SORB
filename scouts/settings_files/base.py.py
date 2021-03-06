'''
Django settings for scouts project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
'''

import os
import django_heroku, dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
os.environ.get('SECRET_KEY', 'SOME+RANDOM+KEY(z9+3vnm(jb0u@&w68t#5_e8s9-lbfhv-')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS =  ['mysterious-hollows-62229.herokuapp.com', '.sorb.com', '127.0.0.1', 'sorb.herokuapp.com']

STRIPE_LIVE_PUBLIC_KEY = ''
STRIPE_LIVE_SECRET_KEY = ''
STRIPE_TEST_PUBLIC_KEY = os.environ.get('STRIPE_TEST_PUBLIC_KEY')
STRIPE_TEST_SECRET_KEY = os.environ.get('STRIPE_TEST_SECRET_KEY')
STRIPE_LIVE_MODE = False


DJSTRIPE_PLANS = {
    "monthly": {
        "stripe_plan_id": "standard-monthly",
        "name": "Web App Pro ($16/month)",
        "description": "The monthly subscription plan to SORB",
        "price": 1600,  # $16.00
        "currency": "aud",
        "interval": "month"
    },
    "yearly": {
        "stripe_plan_id": "standard-yearly",
        "name": "Web App Pro ($160/year)",
        "description": "The annual subscription plan to WebApp",
        "price": 16000,  # $199.00
        "currency": "aud",
        "interval": "year"
    }
}

# Application definition

INSTALLED_APPS = [
#    'grappelli',
    'home',
    'record_book',
    'login',
    'accounts',
    'leaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'djstripe',
    'crequest',

    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'crequest.middleware.CrequestMiddleware',
    'django.middleware.locale.LocaleMiddleware'
#    'audit_log.middleware.UserLoggingMiddleware',
#    'scouts.middleware.LoginRequiredMiddleware',
#    'request_provider.middleware.RequestProvider',

#    'scouts.middleware.ScoutUnautharizationMiddleware'
]

ROOT_URLCONF = 'scouts.urls'

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
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]
WSGI_APPLICATION = 'scouts.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'scouts',
        'USER': 'fhall21',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
#DATABASES['default'] = dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
AUTH_PROFILE_MODULE = 'accounts.UserProfile'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    'leaders/static'
    ]
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'scouts/media')

LOGOUT_REDIRECT_URL = '/login/'

LOGIN_REDIRECT_URL = '/login/'

LOGIN_URL ='/login/'

LOGIN_EXEMPT_URLS = {
    'account/logout/',
    'accout/register',
    'account/profile/reset-password/',
    'account/profile/reset-password/complete',
    'account/profile/reset-password/done/',
    'account/profile/reset-password/confirm/<uidb64>[0-9A-Za-z]-<token>/',
    #leaders app
    'leaders/scout_info/login/'
}
'''
SCOUT_AUTHORIZED_URLS = {
    'account/logout/',
    'accouts/register',
    'account/profile/reset-password/',
    'account/profile/reset-password/complete',
    'account/profile/reset-password/done/',
    'account/profile/reset-password/confirm/<uidb64>[0-9A-Za-z]-<token>/'
    'account/profile/',
    'account/profile/edit',
    'account/password',
    'profile/pioneer/' 


}
'''#finish setting up email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'felix.p.hall@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587


CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True

#if local
'''
CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False
'''

#more deployment stuff
# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
DATABASES['default']['CONN_MAX_AGE'] = 500
# Activate Django-Heroku.
django_heroku.settings(locals())