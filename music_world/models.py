from django.db import models
import uuid

# Create your models here.



class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=100, null=False)
    events_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200, null=False)
    description = models.TextField()

    cover = models.ImageField(upload_to='uploads/%Y/%m/%d')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


