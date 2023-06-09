from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


def cliente_modificado(cambio: str) -> dict:
    info = {
        'titulo': f'Cliente {cambio.title()}',
        'listado': '/clientes/listar',
        'mensajes': [
            f'El cliente ha sido {cambio.lower()} con éxito'
        ]
    }

    return info


def cliente_inexistente(id: int) -> dict:
    info = {
        'titulo': 'Cliente Inexistente',
        'listado': '/clientes/listar',
        'mensajes': [
            f'Lo sentimos, no hemos podido encontrar el cliente que buscabas (Con id: {id})',
            'Prueba intentando con otro'
        ]
    }

    return info
