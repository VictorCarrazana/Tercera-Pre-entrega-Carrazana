

from django.urls import path, include
from producto.urls import ProductoList
from core.views import core_view

urlpatterns = [
    path('', core_view),
    path('', include('producto.urls'), name= 'inicio'),

]
