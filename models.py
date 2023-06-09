"""
Definition of models.
"""

from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']  # Default ordering by the 'order' field
