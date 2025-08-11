import django.db.models as models
from .trip import Trip
class TravelExpense(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(max_length=50)
    amount = models.FloatField()
    date = models.DateField()
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'TravelExpenses'
        indexes = [
            models.Index(fields=['trip']),
            models.Index(fields=['date']),
        ]