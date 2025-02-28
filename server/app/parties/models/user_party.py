from django.db import models

class UserPartie(models.Model):
    is_gm = models.BooleanField()