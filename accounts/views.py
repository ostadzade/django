from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile, User  # Import مدل‌ها

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # استفاده از get_or_create برای جلوگیری از ایجاد پروفایل تکراری
            profile, created = Profile.objects.get_or_create(user=user)
            
            # تنظیم اطلاعات خاص کاربر بر اساس نوع
            if user.user_type == 'admin':
                profile.admin_data = {'access_level': 'full'}
            elif user.user_type == 'expert':
                profile.expert_data = {'specialization': 'GIS'}
            else:
                profile.user_data = {'subscription': 'basic'}
            
            profile.save()
            
            messages.success(request, 'حساب کاربری با موفقیت ایجاد شد!')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور نادرست است')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def profile(request):
    # استفاده از متد get_profile که در مدل User تعریف کردیم
    profile = request.user.get_profile()
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل با موفقیت به‌روزرسانی شد')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    
    return render(request, 'accounts/profile.html', {
        'form': form,
        'user_type': request.user.get_user_type_display()
    })