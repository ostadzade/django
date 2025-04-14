from django.contrib import admin
from .models import (
    Company, Currency, Account, 
    Journal, AccountMove, AccountMoveLine, Partner
)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'fiscalyear_end', 'is_active')
    search_fields = ('name',)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol', 'rate', 'is_active')
    search_fields = ('code', 'name')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'account_type', 'is_active')
    list_filter = ('account_type', 'is_active')
    search_fields = ('code', 'name')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'type', 'is_active')
    list_filter = ('type', 'is_active')
    search_fields = ('code', 'name')

class AccountMoveLineInline(admin.TabularInline):
    model = AccountMoveLine
    extra = 1

@admin.register(AccountMove)
class AccountMoveAdmin(admin.ModelAdmin):
    list_display = ('name', 'journal', 'date', 'state')
    list_filter = ('journal', 'date', 'state')
    inlines = [AccountMoveLineInline]

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'partner_type', 'is_active')
    list_filter = ('partner_type', 'is_active')
    search_fields = ('code', 'name')