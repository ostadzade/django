from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Account, AccountMove

class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = 'accounting/accounts/list.html'
    
    def get_queryset(self):
        return Account.objects.filter(company=self.request.user.profile.company)

class MoveCreateView(LoginRequiredMixin, CreateView):
    model = AccountMove
    fields = ['journal', 'date', 'ref']
    template_name = 'accounting/moves/form.html'
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.company = self.request.user.profile.company
        return super().form_valid(form)

class MoveDetailView(LoginRequiredMixin, DetailView):
    model = AccountMove
    template_name = 'accounting/moves/detail.html'