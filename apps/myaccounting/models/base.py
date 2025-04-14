from django.db import models
from apps.account.models import User

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام شرکت')
    fiscalyear_end = models.DateField(verbose_name='پایان سال مالی')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='ایجاد شده توسط')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name = 'شرکت'
        verbose_name_plural = 'شرکت‌ها'
        ordering = ['name']

    def __str__(self):
        return self.name

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True, verbose_name='کد ارز')
    name = models.CharField(max_length=50, verbose_name='نام ارز')
    symbol = models.CharField(max_length=5, verbose_name='نماد')
    rate = models.DecimalField(max_digits=19, decimal_places=6, default=1.0, verbose_name='نرخ برابری')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    
    class Meta:
        verbose_name = 'ارز'
        verbose_name_plural = 'ارزها'
        ordering = ['code']

    def __str__(self):
        return f"{self.code} ({self.symbol})"