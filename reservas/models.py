from django.db import models
from clientes.models import Cliente
from servicios.models import Servicio
from empleados.models import Empleado
from coordinadores.models import Coordinador


# Create your models here.
class Reserva(models.Model):
    fecha_reserva = models.DateField(auto_now_add=True)
    fecha_servicio = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, limit_choices_to={'activo': True})
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, limit_choices_to={'activo': True})
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, limit_choices_to={'activo': True})
    coordinador = models.ForeignKey(Coordinador, on_delete=models.CASCADE, limit_choices_to={'activo': True})
