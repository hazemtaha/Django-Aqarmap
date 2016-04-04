"""
Django settings for Aqarmap project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(&dxf&s*9xz(qov2v-w@!lppr_%w(tbow9uie^u6q!@^!5h1d!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# email configuration
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
# to test sending email by django it'll output the emails in the console
# instead not valid for productions
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'accounts.apps.AccountsConfig',
    'listings.apps.ListingsConfig',
    'subscribtions.apps.SubscribtionsConfig',
    'points.apps.PointsConfig',
    'projects.apps.ProjectsConfig',
    'properties.apps.PropertiesConfig',
    'search.apps.SearchConfig',
    'user_settings.apps.UserSettingsConfig',
    # before adding this app you have to install it's package from here pip
    # install django-geoposition
    'geoposition',
    # social media
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    # django cities-light
    'cities_light',
    # django crispy-forms
    'crispy_forms',
    # video streaming embed video player
    'embed_video'
]
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Aqarmap.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Aqarmap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_aqarmap',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'hussien660',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
# setting my time zone Eastern European Time
TIME_ZONE = 'EET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'global_static')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'global_media')

# for GeoPositioning on the map
GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}

# sets the default user model to custom made one
AUTH_USER_MODEL = "accounts.UserProfile"

# django-allauth custom signup form
ACCOUNT_SIGNUP_FORM_CLASS = 'accounts.forms.RegisterationForm'

# django-allauth related
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# django-allauth
SITE_ID = 2
# to override the redirection after login or signup to custom url
LOGIN_REDIRECT_URL = 'search:index'
SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
     {'METHOD': 'oauth2',
      'SCOPE': ['email', 'public_profile', 'user_friends'],
      'FIELDS': [
          'id',
          'email',
          'name',
          'first_name',
          'last_name',
          'verified', ],
      'EXCHANGE_TOKEN': True,
      'LOCALE_FUNC': lambda request: 'en_US',
      'VERIFIED_EMAIL': True,
      'VERSION': 'v2.4'
      }}
# django cities-light related settings
CITIES_LIGHT_TRANSLATION_LANGUAGES = ['en']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['EG']
CITIES_LIGHT_INCLUDE_CITY_TYPES = ['PPL', 'PPLA', 'PPLA2', 'PPLA3',
                                   'PPLA4', 'PPLC', 'PPLF', 'PPLG', 'PPLL', 'PPLR', 'PPLS', 'STLMT', ]

# django crispy-forms related settings

CRISPY_TEMPLATE_PACK = 'bootstrap3'

