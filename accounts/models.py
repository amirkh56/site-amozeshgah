from django.db import models

# Create your models here.

class CustomUser (models.Model):
    age = models.PositiveIntegerField(null=True, blank=True)