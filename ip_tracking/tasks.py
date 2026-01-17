from celery import shared_task
from ip_tracking.models import RequestLog, SuspiciousIP
from django.utils.timezone import now, timedelta

@shared_task
def detect_anomalies():
    one_hour_ago = now() - timedelta(hours=1)
    logs = RequestLog.objects.filter(timestamp__gte=one_hour_ago)
    counts = {}
    for log in logs:
        counts[log.ip_address] = counts.get(log.ip_address, 0) + 1

    for ip, count in counts.items():
        if count > 100:
            SuspiciousIP.objects.create(ip_address=ip, reason=f"{count} requests/hour")
