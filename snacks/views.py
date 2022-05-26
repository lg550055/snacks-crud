from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack


class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title", "description", "purchaser"]


class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")
