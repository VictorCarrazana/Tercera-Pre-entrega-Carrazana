from django.shortcuts import render

from django.views.generic import *
from vendedor.models import Vendedor
from vendedor.forms import *
from django.urls import reverse_lazy






# Create your views here.






from .models import Vendedor
class Vendedor_List(ListView):
    model = Vendedor
    template_name = 'vendedor/Lista_vendedor.html'
    context_object_name ='Vendedor'

def vendedor_view(request):
    return render(request, "vendedor/index.html")


class Vendedor_Creat(CreateView):
    model = Vendedor
    template_name = 'vendedor/vendedor-new.html'
    context_object_name = 'Vendedor'
    success_url ='/vendedor-lista'
    fields = ['nombre', 'apellido', 'email', 'legajo']

class VendedorUpdateView(UpdateView):
    model = Vendedor
    template_name = 'vendedor/vendedor-editar.html'
    form_class = vendedorForm
    success_url = '/vendedor-lista'
    

class VendedorDelete(DeleteView):
    model = Vendedor
    template_name = 'vendedor/vendedor-eliminar.html'
    success_url = '/vendedor-lista'
   

   
    


