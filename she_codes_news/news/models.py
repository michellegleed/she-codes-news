from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(default=None)
    # last_modified = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    content = models.TextField()

