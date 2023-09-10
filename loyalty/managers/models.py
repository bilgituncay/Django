from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from djongo import models
from shops.models import Shop

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    shops = models.ManyToManyField(Shop)

    def __str__(self):
        return self.name