

from django.urls import path, include
from producto.urls import *
from core.views import core_view
from cliente.urls import *


urlpatterns = [
    path('', core_view),
    path('', include('producto.urls'), name= 'producto'),
    path('', include('vendedor.urls'), name= 'vendedor'),
    path('', include('cliente.urls'), name='cliente'),
    path('cliente', cliente_view),
    path('producto',producto_view),
    
]
