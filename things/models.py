from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
