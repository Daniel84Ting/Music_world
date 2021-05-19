from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class User(AbstractUser):
    pass

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    

    # class Meta:
    #     verbose_name = _("Profile")
    #     verbose_name_plural = _("Profiles")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Profile_detail", kwargs={"pk": self.pk})
