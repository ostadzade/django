from django.apps import AppConfig

class MyaccountingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.myaccounting'
    verbose_name = 'ماژول حسابداری'
    
    def ready(self):
        # فقط اگر فایل signals دارید این خط را فعال کنید
        try:
            import apps.myaccounting.signals
        except ImportError:
            pass