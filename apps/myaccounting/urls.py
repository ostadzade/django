from django.urls import path
from .views import accounting

app_name = 'accounting'

urlpatterns = [
    path('accounts/', accounting.AccountListView.as_view(), name='account-list'),
    path('moves/new/', accounting.MoveCreateView.as_view(), name='move-create'),
    path('moves/<int:pk>/', accounting.MoveDetailView.as_view(), name='move-detail'),
]