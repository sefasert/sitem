import os
from dotenv import load_dotenv

from pathlib import Path

from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv(os.path.join(BASE_DIR, ".env"))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True
ALLOWED_HOSTS = ["*"]



SITE_ID = 5

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "category",
    "accounts",
    "store",
    "carts",
    "orders",
    "ckeditor",
    #htmx:
    "django_extensions",
    "django_htmx",
    #filter
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "django_htmx.middleware.HtmxMiddleware", #htmx
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'greatkart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "category.context_processors.menu_links",
                "carts.context_processors.counter",
                "category.context_processors.context",
            ],
        },
    },
]

WSGI_APPLICATION = 'greatkart.wsgi.application'


AUTH_USER_MODEL = "accounts.Account"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': '2lpS6Jy8US3rAlhmmdBk',
        'HOST': 'containers-us-west-77.railway.app',
        'PORT': '6159',
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length':6}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = ["greatkart/static"]
STATIC_ROOT = BASE_DIR /"static"



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR /"media"


#mesaj işlemler
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


#eposta işlemler
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "enginelektronikinfo@gmail.com"
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "Engin Elektronik <enginelektronikinfo@gmail.com>"


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CSRF_TRUSTED_ORIGINS = ["https://sitem-production.up.railway.app", "https://www.enginelektronik.xyz", "http://www.enginelektronik.xyz"]
