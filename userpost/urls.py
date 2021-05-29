from django.urls import path
from .views import *


app_name = "posts"

urlpatterns = [
    path("", views_post_index, name="post-index"),
    path("create", views_post, name="post-create"),
    path("show/<uuid:pk>", views_postShow, name="posts_show"),
    path("category/", views_create_category, name="category_create"),
    path("comment/<uuid:post>", views_comment, name="comment_create"),
]
