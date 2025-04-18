from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ایجاد پروفایل فقط برای کاربران جدید"""
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """ذخیره پروفایل فقط اگر وجود داشته باشد"""
    if hasattr(instance, 'profile'):
        instance.profile.save()