from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AccountMove

@receiver(post_save, sender=AccountMove)
def update_account_balances(sender, instance, created, **kwargs):
    """سیگنال برای به‌روزرسانی موجودی حساب‌ها پس از ثبت سند"""
    if instance.state == 'posted':
        for line in instance.lines.all():
            # منطق به‌روزرسانی موجودی حساب‌ها
            pass