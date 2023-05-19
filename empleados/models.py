from django.db import models


# Create your models here.
class Empleado(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    nro_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)
