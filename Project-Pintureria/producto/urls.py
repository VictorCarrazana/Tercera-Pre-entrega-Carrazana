from django.urls import path

from producto.views import *
#from producto.views import producto_view

app_name = "Appproducto"

urlpatterns = [
  path('producto-lista', ProductoList.as_view(), name= 'Producto-list'),
  path('',producto_view, name='Producto'),
  path('producto-nuevo', producto_new_view, name= 'producto-new'),
  path('producto-delete/<pk>', ProductoDelete.as_view(), name= 'Producto-Delete'),
  path('producto-editar/<pk>', ProductoUpdateView.as_view(), name='producto-editar'),
    ]
