
from django.db import models
from .trip import Trip

class Accommodation(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='accommodations')
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Accommodations'
        indexes = [
            models.Index(fields=['trip']),
            models.Index(fields=['date']),
        ]