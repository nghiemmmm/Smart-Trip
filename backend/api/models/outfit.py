import django.db.models as models
from .trip import Trip

class Outfit(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='outfits')
    day = models.IntegerField()
    outfit_name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Outfits'
        indexes = [
            models.Index(fields=['trip']),
            models.Index(fields=['day']),
        ]