from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from servicios.models import Servicio
from coordinadores.models import Coordinador


# Create your views here.
def listar_servicios(request):
    servicios = Servicio.objects.all()
    data = list()

    for servicio in servicios:
        registro = {'id': servicio.id,
                    'nombre': servicio.nombre,
                    'precio': servicio.precio}
        data.append(registro)

    return JsonResponse(data, safe=False)


def obtener_servicio(request, id):
    data = dict()
    try:
        servicio = Servicio.objects.get(id=id)

        data['servicio'] = [
                            {'id': servicio.id,
                             'nombre': servicio.nombre,
                             'descripcion': servicio.descripcion,
                             'precio': servicio.precio}
                            ]

    except ObjectDoesNotExist as e:
        data['servicio'] = []

    finally:
        return JsonResponse(data)


def listar_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    data = list()

    for coordinador in coordinadores:
        registro = {'id': coordinador.id,
                    'nombre': coordinador.nombre,
                    'apellido': coordinador.apellido,
                    'dni': coordinador.dni,
                    'fecha_alta': coordinador.fecha_alta,
                    'activo': coordinador.activo}
        data.append(registro)

    return JsonResponse(data, safe=True)
