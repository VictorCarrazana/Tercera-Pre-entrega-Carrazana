from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=100)
    precio = models.IntegerField ()
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.tamaño}"
    


   