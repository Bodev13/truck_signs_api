import environ
from .base import *

# DEBUG = True

env = environ.Env()
# reading env file
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env('DEBUG')

CORS_ALLOWED_ORIGINS = [
    "https://www.signsfortrucks.com",
    "https://signsfortrucks.com",
    "http://localhost:3000",
]

# ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1',]
ALLOWED_HOSTS = env(
    'ALLOWED_HOSTS', default='localhost,127.0.0.1,0.0.0.0').split(',')


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

STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
