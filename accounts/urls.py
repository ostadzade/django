from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # این خط بسیار مهم است
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]