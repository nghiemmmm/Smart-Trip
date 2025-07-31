from django.db import models
from django.contrib.auth.models import User  # ✅ dùng User mặc định

class UserProfile(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING)  # ✅ thay AuthUser
    preferences = models.JSONField(blank=True, null=True)
    interaction_history = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user_profile'
        managed = False  # giữ nếu bạn không muốn Django quản lý bảng
