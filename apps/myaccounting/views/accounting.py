from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import AccountMove
from ..forms import AccountMoveForm

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'myaccounting/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'dashboard'
        return context

class AccountMoveListView(LoginRequiredMixin, ListView):
    model = AccountMove
    template_name = 'myaccounting/moves/list.html'
    context_object_name = 'moves'
    paginate_by = 20
    
    def get_queryset(self):
        return super().get_queryset().filter(
            company=self.request.user.company
        ).select_related('journal', 'company')

class AccountMoveCreateView(LoginRequiredMixin, CreateView):
    model = AccountMove
    form_class = AccountMoveForm
    template_name = 'myaccounting/moves/form.html'
    success_url = reverse_lazy('myaccounting:move_list')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['company'] = self.request.user.company
        return kwargs
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.company = self.request.user.company
        return super().form_valid(form)

class AccountMoveDetailView(LoginRequiredMixin, DetailView):
    model = AccountMove
    template_name = 'myaccounting/moves/detail.html'
    context_object_name = 'move'
    
    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            'lines', 'lines__account', 'lines__partner'
        )