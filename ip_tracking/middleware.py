# ip_tracking/middleware.py
from django.http import HttpResponseForbidden
from .models import BlockedIP

class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, _ = get_client_ip(request)
        path = request.path

        # Check blacklist
        if ip and BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Your IP has been blocked.")

        # Log request
        if ip:
            RequestLog.objects.create(ip_address=ip, path=path)

        response = self.get_response(request)
        return response
