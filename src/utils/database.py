import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

bd = os.getenv('BD', 'local')

if bd == 'testing':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': os.getenv('DJANGO_DB_NAME', 'django_gst'),
            'USER': os.getenv('DJANGO_DB_USER', 'django'),
            'PASSWORD': os.getenv('DJANGO_DB_PASS', 'django'),
            'HOST': os.getenv('DJANGO_DB_HOST', '192.168.2.71'),
            'PORT': os.getenv('DJANGO_DB_PORT', '3306')
        }
    }
elif bd == 'prod':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': os.getenv('DJANGO_DB_NAME', 'django_gst'),
            'USER': os.getenv('DJANGO_DB_USER', 'django'),
            'PASSWORD': os.getenv('DJANGO_DB_PASS', 'django'),
            'HOST': os.getenv('DJANGO_DB_HOST', '192.168.2.71'),
            'PORT': os.getenv('DJANGO_DB_PORT', '3306')
        }
    }
elif bd == 'local':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
