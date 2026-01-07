# settings.py configuration for Task 2a
# This enables secure REST API communication with the React frontend.

INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Handles CORS headers
    'django.middleware.common.CommonMiddleware',
]

# Security: Restricted access to our specific development domains
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://dev.bharatyuva.org",
]