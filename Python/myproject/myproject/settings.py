"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f&l#t=81c-!f#&s2s(%jc8&gz-cg2$s##+8ay-@wx6id^8rpv%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
#작성된 app은 반드시 등록한다. 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'blog', 
    'scoops',
    'bookmark',  
    'modeltest',
    'shop',
    'book',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INTERNAL_IPS=['127.0.0.1']
ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'myproject','templates'),
          
        ],
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

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }    
}

# 'default':{
    #         'ENGINE': 'django.db.backends.oracle',
    #         "NAME" : 'xe',
    #         'USER' : 'hr',
    #         'PASSWORD' : 'hr',
    #         'HOST' : '127.0.0.1',
    #         'PORT' : '1521',

    # }

# 'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'world', # DB명
#         'USER': 'root', # 데이터베이스 계정
#         'PASSWORD': '1234', # 계정 비밀번호
#         'HOST': '127.0.0.1', # 데이테베이스 주소(IP)
#         'PORT': '3306', # 데이터베이스 포트(보통은 3306)
# }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#static파일의 URL prefix 
STATIC_URL = '/static/'

#개발환경 
STATICFILES_DIRS=[ os.path.join(BASE_DIR, 'myproject', 'static'), 
                   os.path.join(BASE_DIR, 'book', 'static')                  
                  ]

#배포시 ....>>python manage.py collectstatic 
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'staticfiles')

#media파일의 대한 URL prefix
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




AUTH_USER_MODEL = 'auth.User'

