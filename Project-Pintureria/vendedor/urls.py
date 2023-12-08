from django.urls import path

from vendedor.views import Vendedor_List
from vendedor.views import vendedor_view
app_name = "vendedor"

urlpatterns = [
 path('vendedor-lista', Vendedor_List.as_view(), name= 'vendedor_lista'),
 path('vendedor', vendedor_view, name='vendedor'),
]

