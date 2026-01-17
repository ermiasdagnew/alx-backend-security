# alx-backend-security/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx-backend-security.settings')

application = get_asgi_application()
