from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    password_confirmation = models.CharField(max_length=128)
    email = models.EmailField('email', unique=True)
    username = models.CharField(max_length=150, unique=True)


    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []