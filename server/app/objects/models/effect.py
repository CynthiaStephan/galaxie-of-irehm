from django.db import models

class Effects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()