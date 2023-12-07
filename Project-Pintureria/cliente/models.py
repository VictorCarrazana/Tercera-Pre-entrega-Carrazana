from django.db import models

# Create your models here.
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField (null=True, blank=True)
    situacionCrediticia = models.BooleanField( auto_created=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    