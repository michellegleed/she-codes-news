from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where I will put my own fields for the user model.
    pass

    def __str__(self):
        return self.username