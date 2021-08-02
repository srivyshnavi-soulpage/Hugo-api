import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'top-secret!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Inhouse apps
    'hugo.analytics',
    'hugo.api',
    'hugo.bgtasks',
    'hugo.db',
    'hugo.utils',
    'hugo.web',

    # Third-party things
    'rest_framework',
    'corsheaders',
    'taggit',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hugo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
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

WSGI_APPLICATION = 'hugo.wsgi.application'

# Django Sites

SITE_ID = 1

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation

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

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static-assets', 'collected-static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Media Settings
MEDIA_ROOT = 'mediafiles'
MEDIA_URL = '/media/'


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL ="db.User"



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
      
    ],

}
from datetime import timedelta


SIMPLE_JWT = {
   "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
   "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
   "ROTATE_REFRESH_TOKENS": False,
   "BLACKLIST_AFTER_ROTATION": True,
   "UPDATE_LAST_LOGIN": False,
   "ALGORITHM": "HS256",
   "SIGNING_KEY": SECRET_KEY,
   "VERIFYING_KEY": None,
   "AUDIENCE": None,
   "ISSUER": None,
   "AUTH_HEADER_TYPES": ("Bearer",),
   "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
   "USER_ID_FIELD": "id",
   "USER_ID_CLAIM": "user_id",
   "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
   "TOKEN_TYPE_CLAIM": "token_type",
   "JTI_CLAIM": "jti",
   "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
   "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
   "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}