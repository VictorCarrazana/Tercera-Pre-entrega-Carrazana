from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
def producto_view(request):
    return render(request, "producto/index.html")

from .models import Producto
class ProductoList(ListView):
    model = Producto
    template_name = 'producto/index.html'

