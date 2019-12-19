from .common_settings import *

# For better debugging
# This is only for development
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "local_book_store",
        "USER": "localbookstoreuser",
        "PASSWORD": '123',
        "HOST": "localhost",
        "PORT": "",
    }
}

# These the third party apps that
# we need in the development process
DEVELOPMENT_APPS = ()

# This is the variable that django looks for
# to know about the apps that the project uses.
INSTALLED_APPS = EXTERNAL_APPS + DEVELOPMENT_APPS + INTERNAL_APPS


# Media files / the files that we upload
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(PROJECT_PATH, "static")]
