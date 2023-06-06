from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from servicios.models import Servicio
from clientes.models import Cliente


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


def listar_clientes(request):
    clientes = Cliente.objects.all()
    data = list()

    for cliente in clientes:
        registro = {
            'id': cliente.id,
            'nombre' : cliente.nombre,
            'apellido' : cliente.apellido,
            'activo' : cliente.activo
        }
        data.append(registro)
    
    return JsonResponse(data,safe=False)
