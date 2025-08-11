from django.db import models
from .trip import Trip

class Restaurant(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    itinerary_day = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Restaurants'
        indexes = [
            models.Index(fields=['trip']),
            models.Index(fields=['itinerary_day']),
        ]