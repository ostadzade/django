from django.db import models
from .base import BaseModel

class Partner(BaseModel):
    PARTNER_TYPES = [
        ('customer', 'مشتری'),
        ('supplier', 'تامین کننده'),
        ('both', 'هر دو')
    ]
    
    name = models.CharField(max_length=100)
    partner_type = models.CharField(max_length=10, choices=PARTNER_TYPES)
    tax_id = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} ({self.get_partner_type_display()})"