from django.urls import path
from .views import *


app_name = "events"

urlpatterns = [
    path("", views_index, name="musics_index"),
    path("events/", views_event, name="musics_event"),
    path("show/<uuid:pk>", views_show, name="musics_show"),
]
