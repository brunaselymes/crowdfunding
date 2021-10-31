from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=400, blank=True)
    image = models.URLField(max_length=400, blank=True)

    def __str__(self):
        return self.username
