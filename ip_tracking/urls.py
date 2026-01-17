# ip_tracking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # Add other endpoints like analytics or dashboard here
]
