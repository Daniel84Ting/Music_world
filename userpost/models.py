from django.db import models
from accounts.models import User
from django.utils import timezone
from django.urls import reverse
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name

# class Comment(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=False)
#     post = models.ForeignKey('post', on_delete=models.CASCADE)
#     content = models.TextField()

#     def __str__(self):
#         return self.user.username

    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
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


    def get_absolute_url(self):
        return reverse('post-create', kwargs={'pk': self.pk})