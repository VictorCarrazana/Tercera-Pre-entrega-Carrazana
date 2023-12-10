from django.urls import path

from vendedor.views import Vendedor_List
from vendedor.views import *
app_name = "vendedor"

urlpatterns = [
 path('vendedor-lista', Vendedor_List.as_view(), name= 'vendedor_lista'),
 path('vendedor', vendedor_view, name='vendedor'),
 path ('vendedor-new', Vendedor_Creat.as_view(), name = 'vendedor-new'),
 path('vendedor-editar/<pk>', VendedorUpdateView.as_view(),name= 'vendedor-editar'),
 path('vendedor-eliminar/<pk>',VendedorDelete.as_view(), name ='vendedor-editar' ),


]

