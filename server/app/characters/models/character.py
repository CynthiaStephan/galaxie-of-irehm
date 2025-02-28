from django.db import models
class Character(models.Model):
    name = models.CharField(max_length=100)
    story = models.CharField(max_length=255)
    description = models.TextField()
    hair = models.CharField(max_length=50)
    eyes = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    level = models.IntegerField()
    totalxp = models.IntegerField()
    xd = models.IntegerField()
    img = models.CharField(max_length=255)
    