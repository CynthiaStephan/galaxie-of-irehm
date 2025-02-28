from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    website = models.URLField(blank=True)
    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]
    theme = models.CharField(max_length=5, choices=THEME_CHOICES, default='light')
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True)
    last_activity = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email