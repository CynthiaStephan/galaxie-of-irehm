from django.db import models

class Session(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.TextField()
    
    