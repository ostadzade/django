from django.db import models
from django.core.validators import MinValueValidator
from .base import Company, Currency
from .partner import Partner

class Account(models.Model):
    TYPE_CHOICES = [
        ('asset', 'دارایی'),
        ('liability', 'بدهی'),
        ('equity', 'سرمایه'),
        ('income', 'درآمد'),
        ('expense', 'هزینه'),
    ]
    
    code = models.CharField(max_length=20, verbose_name='کد حساب')
    name = models.CharField(max_length=200, verbose_name='نام حساب')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='حساب والد')
    account_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='نوع حساب')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, verbose_name='ارز')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='شرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name = 'حساب'
        verbose_name_plural = 'حساب‌ها'
        unique_together = ('code', 'company')
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - {self.name}"

class Journal(models.Model):
    JOURNAL_TYPES = [
        ('sale', 'فروش'),
        ('purchase', 'خرید'),
        ('cash', 'نقدی'),
        ('bank', 'بانکی'),
        ('general', 'عمومی'),
    ]
    
    code = models.CharField(max_length=10, unique=True, verbose_name='کد دفتر')
    name = models.CharField(max_length=100, verbose_name='نام دفتر')
    type = models.CharField(max_length=10, choices=JOURNAL_TYPES, verbose_name='نوع دفتر')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='شرکت')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    
    class Meta:
        verbose_name = 'دفتر روزنامه'
        verbose_name_plural = 'دفاتر روزنامه'
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - {self.name}"

class AccountMove(models.Model):
    STATE_CHOICES = [
        ('draft', 'پیش‌نویس'),
        ('posted', 'ثبت شده'),
        ('canceled', 'لغو شده'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='شماره سند')
    date = models.DateField(verbose_name='تاریخ سند')
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT, verbose_name='دفتر روزنامه')
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='draft', verbose_name='وضعیت')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='شرکت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین ویرایش')
    
    class Meta:
        verbose_name = 'سند حسابداری'
        verbose_name_plural = 'اسناد حسابداری'
        ordering = ['-date', '-id']

    def __str__(self):
        return f"{self.journal.code}/{self.name}"

class AccountMoveLine(models.Model):
    move = models.ForeignKey(AccountMove, on_delete=models.CASCADE, related_name='lines', verbose_name='سند')
    account = models.ForeignKey(Account, on_delete=models.PROTECT, verbose_name='حساب')
    partner = models.ForeignKey(Partner, on_delete=models.PROTECT, null=True, blank=True, verbose_name='طرف حساب')
    debit = models.DecimalField(
        max_digits=19, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name='بدهکار'
    )
    credit = models.DecimalField(
        max_digits=19, 
        decimal_places=2, 
        default=0,
        validators=[MinValueValidator(0)],
        verbose_name='بستانکار'
    )
    description = models.TextField(blank=True, verbose_name='شرح')
    
    class Meta:
        verbose_name = 'سطر سند'
        verbose_name_plural = 'سطرهای سند'
        ordering = ['id']

    def __str__(self):
        return f"{self.move} - {self.account.code}"