# ip_tracking/middleware.py
from django.core.cache import cache
from ipgeolocation.ipgeolocation import IPGeolocation
import os

API_KEY = os.getenv("IPGEOLOCATION_API_KEY")  # Set in .env

geo = IPGeolocation(API_KEY)

class IPLoggingMiddleware:
    # inside __call__ after IP check
    if ip:
        country, city = None, None
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
        RequestLog.objects.create(ip_address=ip, path=path, country=country, city=city)
