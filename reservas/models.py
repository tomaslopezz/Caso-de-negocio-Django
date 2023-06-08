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


def reserva_modificada(cambio: str) -> dict:
    info = {
        'titulo': f'Reserva {cambio.title()}',
        'listado': '/reservas/listar',
        'mensajes': [
            f'La reserva ha sido {cambio.lower()} con éxito'
        ]
    }

    return info


def reserva_inexistente(id: int) -> dict:
    info = {
        'titulo': 'Reserva Inexistente',
        'listado': '/reservas/listar',
        'mensajes': [
            f'Lo sentimos, no hemos podido encontrar la reserva que buscabas (Con id: {id})',
            'Tal vez la reserva no existe o ya fue eliminada',
            'Prueba intentando con otra'
        ]
    }

    return info
