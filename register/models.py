from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=False)
    phoneNumber = models.CharField(max_length=8, blank=False)

    def __str__(self):
        return self.user.username
