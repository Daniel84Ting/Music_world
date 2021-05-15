from django.urls import path
from .views import *

app_name = 'reviews'

urlpatterns = [
    # path("", views_index, name="reviews_index"),
    path("event/<uuid:event>", views_create, name="review_create"),
]
