from django.urls import path

from producto.views import ProductoList

app_name = "producto"

urlpatterns = [
 path('producto-lista', ProductoList.as_view(), name= 'producto_list')
]


#app_name = "cliente"

#urlpatterns = [
 #   path("", views.home, name="index"),
#]