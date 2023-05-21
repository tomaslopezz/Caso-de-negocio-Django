from django.db import models


# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)


def __str__(self):
    return f'{self.nombre}'
