from django.urls import path
from .views import *

urlpatterns = [
    path("", views_index, name="musics_index"),
]
