"""
Django settings for survmanage project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Suppose we always deploy with docker
IS_DEPLOYED = os.path.exists('/.dockerenv')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7#fcp^uwlm^06ys7==m1i+v+l#++hhl&%_=^&8)mgqnm8kfu_y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'channel',
    'alert',
    'push',
    'system',
    'algorithm',
    'cameradaemon',
    'upload',
    'interface'
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

ROOT_URLCONF = 'survmanage.urls'

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

WSGI_APPLICATION = 'survmanage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE') or 'survmanage',
        'USER': os.environ.get('MYSQL_USERNAME') or 'root',
        'PASSWORD': os.environ.get('MYSQL_PASSWORD') or '12345678',
        'HOST': os.environ.get('MYSQL_HOST') or '127.0.0.1',  # If in docker use mysql's network name
        'PORT': (os.environ.get('MYSQL_PORT') and int(os.environ.get('MYSQL_PORT'))) or 3306,
        'charset': 'utf8mb4',
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# ALERT_IMAGE_DIR = Path(BASE_DIR).joinpath('static').joinpath('images')
DYNAMIC_DATA_PATH = os.environ.get('DYNAMIC_DATA_PATH')
DYNAMIC_FILE_DIR = (DYNAMIC_DATA_PATH and Path(DYNAMIC_DATA_PATH)) or BASE_DIR.parent.joinpath('dynamic')
ALERT_IMAGE_DIR = DYNAMIC_FILE_DIR.joinpath('images')

STATICFILES_DIRS = [
    Path(BASE_DIR).joinpath('static'),
    DYNAMIC_FILE_DIR
]

try:
    ALERT_IMAGE_DIR.mkdir(parents=True)
except:
    pass

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',
                                'rest_framework.filters.SearchFilter',
                                'rest_framework.filters.OrderingFilter'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'EXCEPTION_HANDLER': 'utils.custom_exception.custom_exception_handler',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',  # 提示出错，没有调用process_request方法
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'utils.mypermission.MyPermission',
    ],
}

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080"
]

IMAGE_SERVER_HOST = os.environ.get('IMAGESERVER_HOST') or "localhost"
IMAGE_SERVER_PORT = (os.environ.get('IMAGESERVER_PORT') and int(os.environ.get('IMAGESERVER_PORT'))) or 6790
MODEL_PATH = os.environ.get('MODEL_PATH') or r"E:\data\yolov5-checkpoints\yolov5s.pt"
MODEL_DEVICE = os.environ.get('MODEL_DEVICE') or 'cpu'

AUTHSERVER_HOST = os.environ.get('AUTHSERVER_HOST') or "localhost"
AUTHSERVER_PORT = os.environ.get('AUTHSERVER_PORT') or "9090"
AUTH_SERVER_ROOT = f'http://{AUTHSERVER_HOST}:{AUTHSERVER_PORT}/api/v1/'

AUTH_CHECK_ONLINE = False  # 是否每次连线检查激活状态

UPGRADE_FLAG_FILE = os.environ.get('UPGRADE_FLAG_FILE') or DYNAMIC_FILE_DIR.joinpath('upgrade_flag')
RESET_FLAG_FILE = os.environ.get('RESET_FLAG_FILE') or DYNAMIC_FILE_DIR.joinpath('reset_flag')

UPLOAD_FILE_DIR = os.environ.get('UPLOAD_FILE_DIR') or DYNAMIC_FILE_DIR.joinpath('upload')
try:
    UPLOAD_FILE_DIR.mkdir(parents=False)
except:
    pass

MODEL_TO_ALG_FILE = BASE_DIR.joinpath('model_to_alg_name.json')

NETPLAN_CONFIG_DIR = Path('/etc/netplan').resolve()
if not NETPLAN_CONFIG_DIR.exists():
    NETPLAN_CONFIG_DIR = Path(os.environ.get('USERPROFILE')).resolve()

NETWORK_CONFIG_ETH0 = NETPLAN_CONFIG_DIR.joinpath('01-netcfg.yaml')
NETWORK_CONFIG_WLAN0 = NETPLAN_CONFIG_DIR.joinpath('02-netcfg.yaml')
