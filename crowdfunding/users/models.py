from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return self.username
