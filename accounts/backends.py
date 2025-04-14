from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class UserTypeAuthBackend(ModelBackend):
    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.user_type == 'admin':
            return True
        # منطق بررسی دسترسی‌های خاص بر اساس نوع کاربر
        return super().has_perm(user_obj, perm, obj)