from django.db import models


# Create your models here.
class Coordinador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    fecha_alta = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


def coordinador_modificado(cambio: str) -> dict:
    info = {
        'titulo': f'Coordinador {cambio.title()}',
        'listado': '/coordinadores/listar',
        'mensajes': [
            f'El coordinador ha sido {cambio.lower()} con éxito'
        ]
    }

    return info


def coordinador_inexistente(id: int) -> dict:
    info = {
        'titulo': 'Coordinador Inexistente',
        'listado': '/coordinadores/listar',
        'mensajes': [
            f'Lo sentimos, no hemos podido encontrar el coordinador que buscabas (Con id: {id})',
            'Prueba intentando con otro'
        ]
    }

    return info
