from django.db import models

from django.contrib.auth.models import AbstractUser

from news.models import Category

class CustomUser(AbstractUser):
    bio = models.TextField()
    image_url = models.CharField(max_length=200, blank=True)
    image = models.ImageField(default='default.jpg', upload_to="images/profile/", blank=True)
    favourite_categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.username