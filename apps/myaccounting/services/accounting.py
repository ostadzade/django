from django.db import transaction
from ..models import AccountMove, AccountMoveLine

class AccountingService:
    @classmethod
    def create_move(cls, journal_id, date, lines_data, user):
        """
        ایجاد سند حسابداری جدید
        """
        from ..models import Journal
        
        journal = Journal.objects.get(pk=journal_id)
        
        with transaction.atomic():
            move = AccountMove.objects.create(
                journal=journal,
                date=date,
                company=user.company,
                created_by=user,
                state='draft'
            )
            
            lines = []
            for line in lines_data:
                lines.append(AccountMoveLine(
                    move=move,
                    account_id=line['account_id'],
                    partner_id=line.get('partner_id'),
                    debit=line.get('debit', 0),
                    credit=line.get('credit', 0),
                    description=line.get('description', '')
                ))
            
            AccountMoveLine.objects.bulk_create(lines)
            
            # اعتبارسنجی تراز سند
            total_debit = sum(line.debit for line in lines)
            total_credit = sum(line.credit for line in lines)
            
            if total_debit != total_credit:
                raise ValueError("جمع دفتری و بستانکاری باید برابر باشند.")
            
            return move

    @classmethod
    def post_move(cls, move_id):
        """
        ثبت سند حسابداری
        """
        from ..models import AccountMove
        
        move = AccountMove.objects.get(pk=move_id)
        
        with transaction.atomic():
            if move.state != 'draft':
                raise ValueError("فقط اسناد پیش‌نویس قابل ثبت هستند.")
            
            move.state = 'posted'
            move.save()
            
            # به‌روزرسانی مانده حساب‌ها
            for line in move.lines.all():
                line.account.update_balance()
            
            return move