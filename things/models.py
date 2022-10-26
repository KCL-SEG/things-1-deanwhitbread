from django.db import models

class Thing(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=80)
    quantity = models.PositiveIntegerField()

# Create your models here.
