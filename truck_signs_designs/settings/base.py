"""
Django settings for truck_signs_designs project.

Generated by 'django-admin startproject' using Django 2.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import environ
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
TEMPLATES_DIR = os.path.join(ROOT_BASE_DIR, 'templates')

env = environ.Env()
# reading env file
environ.Env.read_env()
environ.Env.read_env(os.path.join(
    BASE_DIR, 'truck_signs_designs', 'settings', '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist


SECRET_KEY = env("DOCKER_SECRET_KEY")
DEBUG = env.bool('DEBUG', default=False)


# ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1',]
ALLOWED_HOSTS = env(
    'ALLOWED_HOSTS', default='localhost,127.0.0.1,0.0.0.0').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'cloudinary',
    'backend',
    'django.contrib.admin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'truck_signs_designs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'truck_signs_designs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(ROOT_BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(ROOT_BASE_DIR, 'static/')

# STATICFILES_FINDERS = (
# 'django.contrib.staticfiles.finders.FileSystemFinder',
# 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_BASE_DIR, 'media')

# STRIPE_PUBLISHABLE_KEY=os.getenv("STRIPE_PUBLISHABLE_KEY")
# STRIPE_SECRET_KEY=os.getenv("STRIPE_SECRET_KEY")


# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Activate Django-Heroku.
