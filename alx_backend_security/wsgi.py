import os
from django.core.wsgi import get_wsgi_application

# Make sure this matches your package folder name
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_security.settings")

application = get_wsgi_application()
