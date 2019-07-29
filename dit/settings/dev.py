import dj_database_url

from dit.settings.base import *

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
