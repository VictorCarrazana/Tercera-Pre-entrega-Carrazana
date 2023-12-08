from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
# Create your views here.

from .models import Vendedor
class Vendedor_List(ListView):
    model = Vendedor
    template_name = 'vendedor/Lista_vendedor.html'

def vendedor_view(request):
    return render(request, "vendedor/index.html")
