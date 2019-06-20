from dit.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'root',
        'HOST': 'db',
        'PORT': 5432,
    }
}
