from music_world.models import Event
from django.utils import timezone
from django.db import models
import uuid
from accounts.models import User
# Create your models here.

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=200, null=True)
    review = models.TextField(null=False)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    



    def __str__(self):
        return self.review