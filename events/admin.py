from django.contrib import admin
from .models import Event, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'date', 'location')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event',
        'email',
        'college_name',
        'department',
        'current_year'
    )

    search_fields = (
        'name',
        'email',
        'college_name'
    )