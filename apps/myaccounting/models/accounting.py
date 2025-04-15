from django.db import models
from .base import BaseModel

class AccountType(models.TextChoices):
    ASSET = 'ASSET', 'دارایی'
    LIABILITY = 'LIABILITY', 'بدهی'
    EQUITY = 'EQUITY', 'سرمایه'
    INCOME = 'INCOME', 'درآمد'
    EXPENSE = 'EXPENSE', 'هزینه'

class Account(BaseModel):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, 
                             null=True, blank=True)
    account_type = models.CharField(max_length=10, 
                                  choices=AccountType.choices)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    reconcile = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('company', 'code')
        ordering = ['code']
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Journal(BaseModel):
    JOURNAL_TYPES = [
        ('sale', 'فروش'),
        ('purchase', 'خرید'),
        ('cash', 'نقدی'),
        ('bank', 'بانکی'),
        ('general', 'عمومی')
    ]
    
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    type = models.CharField(max_length=10, choices=JOURNAL_TYPES)
    default_account = models.ForeignKey(Account, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

class AccountMove(BaseModel):
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT)
    date = models.DateField()
    ref = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=10, choices=[
        ('draft', 'پیش‌نویس'),
        ('posted', 'ثبت شده'),
        ('canceled', 'لغو شده')
    ], default='draft')
    
    class Meta:
        ordering = ['-date', '-id']
    
    def __str__(self):
        return f"{self.journal.code}/{self.id}"

class AccountMoveLine(models.Model):
    move = models.ForeignKey(AccountMove, on_delete=models.CASCADE,
                           related_name='lines')
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    partner = models.ForeignKey('Partner', on_delete=models.SET_NULL,
                              null=True, blank=True)
    debit = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    amount_currency = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    reconciled = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.move} - {self.account}"