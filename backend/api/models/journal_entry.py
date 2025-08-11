import django.db.models as models
from .trip import Trip

class JournalEntry(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='journal_entries')
    date = models.DateField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'JournalEntries'
        indexes = [
            models.Index(fields=['trip']),
            models.Index(fields=['date']),
        ]