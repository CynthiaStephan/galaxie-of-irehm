from django.db import models

class InventiryObject(models.Model):
    is_equiped = models.BooleanField()