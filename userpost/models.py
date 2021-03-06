from django.db import models
from accounts.models import User
from django.urls import reverse
import uuid

# Create your models here.
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    name = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name


    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    events_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200, null=False)
    description = models.TextField()
    

    cover = models.ImageField(upload_to='uploads/%Y/%m/%d')
    categories = models.ManyToManyField(Category, related_name='posts')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-create', kwargs={'pk': self.pk})


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    

    comment = models.TextField(null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    
