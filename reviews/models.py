from music_world.models import Event
from accounts.models import User
from django.utils import timezone
from django.db import models
import uuid

# Create your models here.

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reviews')


    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "review": self.review,
            "event": {
                "title": self.event.title
            }
        }

    def __str__(self):
        return self.review