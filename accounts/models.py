from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True
    )

    goal = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.user.username