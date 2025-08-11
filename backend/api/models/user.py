from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser

# Mô hình User (mở rộng AbstractUser)
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Đảm bảo email là duy nhất
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]