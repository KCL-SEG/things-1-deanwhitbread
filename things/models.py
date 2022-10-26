from django.db import models
from django.core.exceptions import ValidationError

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.PositiveIntegerField(validator=[validate_quantity_range])

    def validate_quantity_range(value):
        if not (value <= 100 and value >= 0):
            raise ValidationError()

# Create your models here.
