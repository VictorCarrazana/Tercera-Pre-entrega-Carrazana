from django.urls import path

from .views import cliente_view


app_name = "cliente"

urlpatterns = [
 path('', cliente_view, name= 'cliente' ),
 
]


