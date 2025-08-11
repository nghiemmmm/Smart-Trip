from django.db import models

# Mô hình Trip
class Trip(models.Model):
    user = models.ForeignKey(
        'api.User',  # Tham chiếu tới model User trong app api
        on_delete=models.CASCADE,
        related_name='trips'
    )
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    trip_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Trips'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['start_date']),
        ]
