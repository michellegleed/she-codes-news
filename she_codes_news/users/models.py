from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField()
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.username