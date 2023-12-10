from django import forms

class Producto_Form(forms.Form):
    nombre = forms.CharField()
    marca = forms.CharField()
    tamaño = forms.CharField()
    precio = forms.IntegerField ()
    stock = forms.IntegerField()
    

from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tamaño', 'marca', 'precio', 'stock']