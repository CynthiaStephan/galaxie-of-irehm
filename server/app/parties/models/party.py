from django.db import models

class Partie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.TextField()