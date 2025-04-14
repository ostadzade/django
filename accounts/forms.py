from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

class UserRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPES, label='نوع کاربر')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'organization', 'admin_data', 'expert_data', 'user_data']