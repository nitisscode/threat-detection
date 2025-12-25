from django.contrib import admin
from .models import User, Event, Alert
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'role']
    search_fields = ['email', 'first_name', 'last_name']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['source', 'event_type', 'severity', 'description']
    search_fields = ['source', 'event_type', 'severity', 'description']

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['event', 'status']
    search_fields = ['event', 'status']