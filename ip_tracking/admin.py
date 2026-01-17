# ip_tracking/admin.py
from django.contrib import admin
from .models import RequestLog, BlockedIP, SuspiciousIP

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'path', 'timestamp', 'country', 'city')
    list_filter = ('country', 'city', 'timestamp')
    search_fields = ('ip_address', 'path')

@admin.register(BlockedIP)
class BlockedIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)
    search_fields = ('ip_address',)

@admin.register(SuspiciousIP)
class SuspiciousIPAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'reason', 'flagged_at')
    list_filter = ('reason', 'flagged_at')
    search_fields = ('ip_address',)
