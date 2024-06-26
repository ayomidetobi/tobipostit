"""
Django settings for auth project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
import os
from decouple import config
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-5mzg-!p&21x@)m&u83o3-sx5jo-3e$jq8=edxx^n$+t(=l0!a1'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG = config('DEBUG')
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    # 'corsheaders',
    'djoser',
    'social_django',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    "phonenumber_field",
    'whitenoise'
]

MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
SIMPLE_JWT = {
'AUTH_HEADER_TYPES': ('JWT',),
'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
'AUTH_TOKEN_CLASSES': (
'rest_framework_simplejwt.tokens.AccessToken',
)
}




EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_USE_SSL = config('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL=config('DEFAULT_FROM_EMAIL')


DJOSER = {
'LOGIN_FIELD': 'username',
'USER_CREATE_PASSWORD_RETYPE': True,
'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
'SEND_CONFIRMATION_EMAIL': True,
'SET_USERNAME_RETYPE': True,
'SET_PASSWORD_RETYPE': True,
'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
# 'PASSWORD_RESET_CONFIRM_RETYPE':True,
'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
'ACTIVATION_URL': 'activate/{uid}/{token}',
'SEND_ACTIVATION_EMAIL': True,

'SERIALIZERS': {
'user_create': 'accounts.serializers.UserCreateSerializer',
'user': 'accounts.serializers.UserCreateSerializer',
'current_user': 'accounts.serializers.UserCreateSerializer',
'user_delete': 'djoser.serializers.UserDeleteSerializer',
},
'EMAIL':{
'activation': 'djoser.email.ActivationEmail',
'confirmation': 'djoser.email.ConfirmationEmail',
'password_reset': 'djoser.email.PasswordResetEmail',
'password_changed_confirmation': 'djoser.email.PasswordChangedConfirmationEmail',
'username_changed_confirmation': 'djoser.email.UsernameChangedConfirmationEmail',
'username_reset': 'djoser.email.UsernameResetEmail',
}
}

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:5173','http://localhost:4173','http://localhost:3000', 'http://localhost:4200','http://127.0.0.1:5173'
# ]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)


AUTH_USER_MODEL = 'accounts.UserAccount'


ROOT_URLCONF = 'auth.urls'
TEMPLATES_DIRS=os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'auth.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': dj_database_url.config(
#         # Feel free to alter this value to suit your needs.
#         default='postgresql://postgres:Tobiloba12@localhost:16055/ft9ja',
#         conn_max_age=600
#     )
# }
DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default=config('DATABASE_URL'),
        conn_max_age=600
    )
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


JAZZMIN_SETTINGS = {
    'show_ui_builder': True,
}
JAZZMIN_UI_TWEAKS = {
    "accent": "accent-orange",
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-primary",
    "navbar": "navbar-danger navbar-dark",
    "theme": "superhero",
    "dark_mode_theme": "superhero",
    #  "sidebar": "sidebar-dark-fuchsia",
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
