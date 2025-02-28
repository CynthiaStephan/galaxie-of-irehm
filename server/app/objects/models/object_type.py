from django.db import models

class ObjectType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_equipable = models.BooleanField()
    