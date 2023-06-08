from django.db import models


# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nro_legajo = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


def empleado_modificado(cambio: str) -> dict:
    info = {
        'titulo': f'Empleado {cambio.title()}',
        'listado': '/empleados/listar',
        'mensajes': [
            f'El empleado ha sido {cambio.lower()} con éxito'
        ]
    }

    return info


def empleado_inexistente(id: int) -> dict:
    info = {
        'titulo': 'Empleado Inexistente',
        'listado': '/empleados/listar',
        'mensajes': [
            f'Lo sentimos, no hemos podido encontrar el empleado que buscabas (Con id: {id})',
            'Prueba intentando con otro'
        ]
    }

    return info
