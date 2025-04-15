from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    مدل کاربر سفارشی که جایگزین مدل User پیش‌فرض جنگو می‌شود
    """
    USER_TYPE_CHOICES = (
        ('admin', 'مدیر'),
        ('expert', 'کارشناس'),
        ('client', 'مشتری'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

class Profile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()