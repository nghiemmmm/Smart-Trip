"""
Travel Mate helps decide the destination by providing tourist spots,
interesting trivia, local trends, weather and much more about over 10k cities.
"""
from django.db import models
from django.contrib.auth.models import User  # ✅ dùng User mặc định

class TravelPlan(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)  # ✅ sửa dòng này
    destination = models.CharField(max_length=100)
    accommodation = models.TextField(blank=True, null=True)
    transportation = models.TextField(blank=True, null=True)
    itinerary = models.JSONField(blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'travel_plan'
        managed = False  # ⚠️ giữ nếu bạn không muốn Django tạo bảng này
