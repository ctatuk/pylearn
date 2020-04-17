#database
#https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'DEFAULT': {
        'ENGINE': 'django.db.backendssqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}