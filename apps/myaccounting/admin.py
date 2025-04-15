from django.contrib import admin
from .models import (
    Account, 
    Journal, 
    AccountMove, 
    AccountMoveLine, 
    Partner, 
    Company, 
    Currency
)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'account_type', 'parent')
    list_filter = ('account_type', 'is_active')
    search_fields = ('code', 'name')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'type')
    list_filter = ('type',)

@admin.register(AccountMove)
class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'journal', 'date', 'ref', 'state')
    list_filter = ('journal', 'state', 'date')

@admin.register(AccountMoveLine)
class MoveLineAdmin(admin.ModelAdmin):
    list_display = ('move', 'account', 'debit', 'credit')
    list_filter = ('account',)

admin.site.register(Partner)
admin.site.register(Company)
admin.site.register(Currency)