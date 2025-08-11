
from django.db import models
from api.models.trip import Trip

class Activity(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=100)
    location = models.TextField(blank=True, null=True)
    activity_time = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Activities'
        indexes = [
            models.Index(fields=['trip']),
            models.Index(fields=['activity_time']),
        ]