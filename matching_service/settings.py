# Ajouter les applications
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'corsheaders',
    'user_matching',
    'api',
    'channels',
]

# Middleware pour CORS
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ... autres middlewares
]

# Configuration CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:3000",
]

# Configuration de la base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'matching_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configuration pour channels (WebSockets)
ASGI_APPLICATION = 'matching_service.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}