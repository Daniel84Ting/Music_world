from django.contrib import admin
from music_world.models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ("title","events_date_time","location","created_at")
admin.site.register(Event, EventAdmin)