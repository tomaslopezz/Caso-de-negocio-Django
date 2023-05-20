from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    activo = models.BooleanField(default=True)
