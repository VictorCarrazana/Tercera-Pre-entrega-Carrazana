from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField (null=True, blank=True)
    legajo = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}, Legajo n°{self.legajo}"
    