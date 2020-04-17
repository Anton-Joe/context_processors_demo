from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    password = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    telephone = models.CharField(max_length=30)
