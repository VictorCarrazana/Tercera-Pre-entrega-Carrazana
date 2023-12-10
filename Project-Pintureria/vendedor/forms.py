from django import forms
from .models import Vendedor

class vendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido', 'email', 'legajo', ]


