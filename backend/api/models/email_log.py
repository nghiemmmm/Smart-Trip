"""
Tự động gửi email lịch trình.
"""
from django.db import models
from django.contrib.auth.models import User  # ✅ dùng model mặc định

from .travel_plan import TravelPlan


class EmailLog(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)  # ✅ sửa lại dòng này
    travel_plan = models.ForeignKey('TravelPlan', models.DO_NOTHING)
    sent_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)
    error_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_log'
