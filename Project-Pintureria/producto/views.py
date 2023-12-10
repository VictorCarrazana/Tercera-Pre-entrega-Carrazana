from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Producto
from .forms import Producto_Form, ProductoForm
from django.urls import reverse_lazy

# Create your views here.
def producto_view(request):
    return render(request, "producto/index.html")
# Crear nueva entrada al modelo
def producto_new_view(request):


    if request.method == 'POST':
        miFormulario = Producto_Form(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            producto = Producto( nombre = data['nombre'],  marca= data['marca'], tamaño = data['tamaño'], precio = data['precio'],  stock = data['stock'])
            producto.save()

            return redirect("/producto-lista")
        
        pass

    else:

        miFormulario = Producto_Form()

        return render(request, "producto/producto-nuevo.html", {"miFormulario": miFormulario})

 
# Lista de Productos (catálogo)
from .models import Producto
class ProductoList(ListView):
    model = Producto
    template_name = 'producto/producto-lista.html'
    context_object_name = 'Producto'

#Eliminar registro de modelo

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'producto/producto-Delete.html'
    success_url = '/producto-lista'
    
#Editar registro de modelo



class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto-editar.html'
    success_url = '/producto-lista'