from django.db import models
from .base import BaseModel

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=5)
    rate = models.DecimalField(max_digits=20, decimal_places=6, default=1.0)
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class Company(models.Model):
    name = models.CharField(max_length=100)
    fiscalyear_start = models.DateField()
    fiscalyear_end = models.DateField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name