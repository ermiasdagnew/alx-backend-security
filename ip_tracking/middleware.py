# ip_tracking/middleware.py
from django.http import HttpResponseForbidden
from ipware import get_client_ip
from django.core.cache import cache
from ip_tracking.models import RequestLog, BlockedIP
from ipgeolocation.ipgeolocation import IPGeolocation
import os

API_KEY = os.getenv("IPGEOLOCATION_API_KEY")  # Add this to your environment
geo = IPGeolocation(API_KEY)

class IPTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip, _ = get_client_ip(request)
        path = request.path

        # Block blacklisted IPs
        if ip and BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Your IP has been blocked.")

        country, city = None, None

        # Get geolocation from cache or API
        if ip:
            cache_key = f"geo_{ip}"
            geo_data = cache.get(cache_key)
            if geo_data:
                country, city = geo_data['country'], geo_data['city']
            else:
                try:
                    geo_info = geo.get_geolocation(ip)
                    country = geo_info.get("country_name")
                    city = geo_info.get("city")
                    cache.set(cache_key, {'country': country, 'city': city}, 86400)  # 24h
                except:
                    pass

            # Log the request
            RequestLog.objects.create(ip_address=ip, path=path, country=country, city=city)

        response = self.get_response(request)
        return response
