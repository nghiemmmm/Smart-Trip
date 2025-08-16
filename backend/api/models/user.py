from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """Custom manager cho User model (dùng email để login)"""

    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        """Tạo user mới"""
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        email = self.normalize_email(email)
        username = username.strip()
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Tạo superuser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)   # Email duy nhất
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'   # Đăng nhập bằng email
    REQUIRED_FIELDS = ['username']   # Vẫn giữ username như một field phụ

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
        ]
