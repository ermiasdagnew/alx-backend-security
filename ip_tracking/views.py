# ip_tracking/views.py
from django.http import JsonResponse
from ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', method='GET', block=True)  # anonymous
def login_view(request):
    # Your login logic here
    return JsonResponse({"status": "ok"})
