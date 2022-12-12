from .base import *

DATABASES = {
    'default' :{
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'esquemaprueba',
        'USER' : 'root',
        'PASSWORD' : 'lautaro2004',
        'HOST' : 'localhost',
        'PORT' : '3306'
    }
}