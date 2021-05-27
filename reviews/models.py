from music_world.models import Event
from django.utils import timezone
from django.db import models
import uuid

# Create your models here.

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=200, null=False)
    review = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='reviews')


    def __str__(self):
        return self.review