"""
Django settings for fitWeb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import pdb
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g%jx+23y8@yt#hs95$d&tz2gkx&66adtqsfy_q^59ae4)oy6d^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'fitWeb.apps.index',
    #'tinymce'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #'django.middleware.cache.UpdateCacheMiddleware',
    #'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'fitWeb.urls'

WSGI_APPLICATION = 'fitWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'fitweb',
        'USER':'root',
        'PASSWORD':'viviana',  
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

#MEDIA_ROOT = 'fitWeb/media/'
#MEDIA_URL = 'media'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__)) 
TEMPLATE_DIRS=(os.path.join(RUTA_PROYECTO, "plantilla"),)
STATICFILES_DIRS=(os.path.join(RUTA_PROYECTO, "static"),)
#Establecer la aplicacion para el perfil
AUTH_PROFILE_MODULE = "cliente.cliente"
#para acceder al perfil creado llamamos al metodo user.get_profile()
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'viviana_kitty@ymail.com'
EMAIL_HOST_PASSWORD = 'BarbieGir1'
EMAIL_PORT = 587

#CACHES = {
 #   'default': {
  #      'BACKEND': 'django.core.cache.backends.memcached.MencachedCache',
   #     'LOCATION': '127.0.0.1:11211',
    #}
#}