from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
    )
from .models import Loan
from .forms import LoanForm
from django.shortcuts import get_object_or_404
# Create your views here.


class LoanListView(ListView):
    model = Loan
    context_object_name = 'items'
    template_name = 'loan/index.html'


class LoanCreateView(CreateView):
    form_class = LoanForm
    model = Loan
    template_name = 'loan/loan-form.html'
    success_url = reverse_lazy('index')


class LoanUpdateView(UpdateView):
    form_class = LoanForm
    model = Loan
    template_name = 'loan/loan-form.html'
    success_url = reverse_lazy('index')

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'loan/delete-confirm.html'
    success_url = reverse_lazy('index')


class LoanDetailView(DetailView):
    model = Loan
    context_object_name = 'item'
    template_name = 'loan/detail.html'
