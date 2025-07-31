'''
Kiểm tra và phê duyệt (Human-in-the-Loop).
'''
from django.db import models
class Approval(models.Model):
    travel_plan = models.ForeignKey('TravelPlan', models.DO_NOTHING)
    approved = models.BooleanField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'approval'

