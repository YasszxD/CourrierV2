from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=30, blank=False)
    postal_code = models.CharField(max_length=4, blank=False)
    phone_number = models.CharField(max_length=8, blank=False)

    def __str__(self):
        return self.user.username


class Courier(models.Model):
    recieverFullName = models.CharField(max_length=30, null=True, blank=False)
    recieverAddress = models.CharField(max_length=30, null=True, blank=False)
    recieverPhoneNumber = models.CharField(max_length=8, null=True, blank=False)
    description = models.TextField(max_length=300, blank=False)
    weight = models.CharField(max_length=4, blank=False)
    price = models.IntegerField(null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
