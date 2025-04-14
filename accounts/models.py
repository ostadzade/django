from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    USER_TYPES = (
        ('admin', 'مدیر سیستم'),
        ('expert', 'کارشناس'),
        ('user', 'کاربر معمولی'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='user')
    gis_permissions = models.JSONField(default=dict, blank=True)
    
    def get_profile(self):
        """متد کمکی برای دسترسی به پروفایل"""
        return Profile.objects.get_or_create(user=self)[0]

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'  # مهم: اضافه کردن related_name
    )
    phone = models.CharField(max_length=15, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    
    # مشخصات خاص هر نوع کاربر
    admin_data = models.JSONField(default=dict, blank=True)
    expert_data = models.JSONField(default=dict, blank=True)
    user_data = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# سیگنال‌ها برای ایجاد خودکار پروفایل
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()