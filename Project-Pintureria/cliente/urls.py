from django.urls import path

from cliente.views import *


app_name = "Appcliente"

urlpatterns = [
    path('', cliente_view, name= 'cliente' ),
    path('cliente-lista', cliente_lista.as_view(), name='cliente-lista' ),
    path('cliente-new', cliente_new.as_view(), name= 'cliente-new'),
    path('cliente-editar/<pk>', cliente_editar.as_view(), name= 'cliente_editar'),
    path('cliente-delete/<pk>',cliente_delete.as_view(), name= 'cliente-delete')
 
  ]

