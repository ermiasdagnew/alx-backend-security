# alx-backend-security/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ip-tracking/', include('ip_tracking.urls')),  # you can create ip_tracking/urls.py
]
