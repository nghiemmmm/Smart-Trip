"""
Travel Mate helps decide the destination by providing tourist spots,
interesting trivia, local trends, weather and much more about over 10k cities.
"""
from django.db import models
from .trip import Trip


# Mô hình Itinerary
class Itinerary(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='itineraries')
    day_number = models.IntegerField()
    activity = models.TextField()
    time = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Itinerary'
        indexes = [
            models.Index(fields=['trip']),
            models.Index(fields=['day_number']),
        ]