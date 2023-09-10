from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from djongo import models

class ShopAbstract(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    
class Shop(ShopAbstract):
    pass