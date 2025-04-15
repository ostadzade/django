from decimal import Decimal
from django.db import transaction
from ..models.accounting import AccountMove, AccountMoveLine

class AccountingService:
    @staticmethod
    @transaction.atomic
    def create_move(journal, date, lines, ref='', created_by=None):
        move = AccountMove.objects.create(
            journal=journal,
            date=date,
            ref=ref,
            state='draft',
            created_by=created_by,
            company=journal.company
        )
        
        total_debit = Decimal('0')
        total_credit = Decimal('0')
        
        for line in lines:
            line['move'] = move
            AccountMoveLine.objects.create(**line)
            total_debit += line.get('debit', Decimal('0'))
            total_credit += line.get('credit', Decimal('0'))
        
        if total_debit != total_credit:
            raise ValueError("جمع دفتر و بستانکار باید برابر باشد")
        
        return move

    @staticmethod
    @transaction.atomic
    def post_move(move):
        if move.state != 'draft':
            raise ValueError("فقط اسناد پیش‌نویس قابل ثبت هستند")
        
        move.state = 'posted'
        move.save()
        return move