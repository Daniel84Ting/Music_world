from django.urls import path
from .views import *
from . import views

app_name = "posts"

urlpatterns = [
    path("", views_index, name="musics_index"),
    path("posts/", views_post, name="musics_post"),
    path("show/<uuid:pk>", views_postShow, name="posts_show"),
    path("category/", views_create_category, name="category_create"),
]
