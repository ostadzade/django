from django.db import models
from .base import Company

class Partner(models.Model):
    PARTNER_TYPES = [
        ('customer', 'مشتری'),
        ('supplier', 'تامین کننده'),
        ('both', 'هر دو'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='نام طرف حساب')
    code = models.CharField(max_length=20, verbose_name='کد طرف حساب')
    partner_type = models.CharField(max_length=10, choices=PARTNER_TYPES, verbose_name='نوع طرف حساب')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='شرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name = 'طرف حساب'
        verbose_name_plural = 'طرف‌حساب‌ها'
        unique_together = ('code', 'company')
        ordering = ['name']

    def __str__(self):
        return f"{self.code} - {self.name}"