import os

from django.core.asgi import get_asgi_application


[pytest]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviemanager.settings')

application = get_asgi_application()
