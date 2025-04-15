"""
Django settings for mygis project.

Generated by 'django-admin startproject' using Django 5.2.
"""

from pathlib import Path
from django.contrib.messages import constants as messages
import os  # اضافه شده برای مدیریت مسیرها

# تنظیمات پیام‌ها
MESSAGE_TAGS = {
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# مسیرهای پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# امنیت
SECRET_KEY = 'django-insecure-sv+tpcgx3_g@-dyq^u9!%dh#w$$r)+qeyyrid&7vz)n8rx54g1'
DEBUG = True
ALLOWED_HOSTS = ['*']  # تغییر یافته برای توسعه

# نرم‌افزارهای نصب شده
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'crispy_forms',
    'crispy_bootstrap5',
    'apps.myaccounting',
   ]

# تنظیمات Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# میدل‌ورها
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLها و تمپلیت‌ها
ROOT_URLCONF = 'mygis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # برای فایل‌های عمومی
        'APP_DIRS': True,  # برای تمپلیت‌های داخل اپلیکیشن‌ها
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]

WSGI_APPLICATION = 'mygis.wsgi.application'

# پایگاه داده
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydjangodb',
        'USER': 'myuser',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# اعتبارسنجی رمز عبور
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

# بین‌المللی‌سازی
LANGUAGE_CODE = 'fa-ir'  # تغییر یافته به فارسی
TIME_ZONE = 'Asia/Tehran'  # تغییر یافته به زمان تهران
USE_I18N = True
USE_L10N = True
USE_TZ = True

# فایل‌های استاتیک
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # اضافه شده
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # اضافه شده

MEDIA_URL = '/media/'  # اضافه شده
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # اضافه شده

# تنظیمات احراز هویت
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = [
    'accounts.backends.UserTypeAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_REDIRECT_URL = 'profile'  # اضافه شده
LOGOUT_REDIRECT_URL = 'login'  # اضافه شده

# تنظیمات ایمیل (برای توسعه)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # اضافه شده