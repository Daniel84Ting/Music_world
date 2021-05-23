from django.db import models
# from accounts.models import User
from django.utils import timezone
import uuid

# from django.urls.base import reverse

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # username = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    events_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200, null=False)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    cover = models.ImageField(upload_to='uploads/%Y/%m/%d')
    categories = models.ManyToManyField(Category, related_name='events')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("musics_show", kwargs={"pk": self.pk})