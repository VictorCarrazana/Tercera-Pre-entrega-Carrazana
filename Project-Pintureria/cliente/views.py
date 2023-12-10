from django.shortcuts import render

from django.views.generic import *
from cliente.models import Cliente
from cliente.forms import *
from django.urls import reverse_lazy

# Create your views here.


# Create your views here.
def cliente_view (request):
    return render(request, "cliente/index.html")



class cliente_lista(ListView):
    model = Cliente
    template_name = 'cliente/clientes-lista.html'
    context_object_name = 'Cliente'

   
    
class cliente_new(CreateView):
    model = Cliente
    template_name = 'cliente/clientes-new.html'
    context_object_name = 'Cliente'
    fields = ['nombre', 'apellido', 'email', 'situacionCrediticia', ]
    success_url= '/cliente-lista'

class cliente_editar(UpdateView):
    model = Cliente
    form_class = clienteForm
    template_name = 'cliente/clientes-editar.html'
    success_url = '/cliente-lista'


class cliente_delete(DeleteView):
    model = Cliente
    template_name = 'cliente/cliente-eliminar.html'
    success_url = '/cliente-lista'



