from django.db import models


# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    precio = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre}'


def servicio_modificado(cambio: str) -> dict:
    info = {
        'titulo': f'Servicio {cambio.title()}',
        'listado': '/servicios/listar',
        'mensajes': [
            f'El servicio ha sido {cambio.lower()} con éxito'
        ]
    }

    return info


def servicio_inexistente(id: int) -> dict:
    info = {
        'titulo': 'Servicio Inexistente',
        'listado': '/servicios/listar',
        'mensajes': [
            f'Lo sentimos, no hemos podido encontrar el servicio que buscabas (Con id: {id})',
            'Prueba intentando con otro'
        ]
    }

    return info
