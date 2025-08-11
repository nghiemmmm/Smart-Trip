import django.db.models as models
from .trip import Trip

class PackingList(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='packing_list')
    item_name = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'PackingList'
        indexes = [
            models.Index(fields=['trip']),
        ]