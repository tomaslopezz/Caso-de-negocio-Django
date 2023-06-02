from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from servicios.models import Servicio


# Create your views here.
def listar_servicios(request):
    servicios = Servicio.objects.all()
    json = []

    for servicio in servicios:
        data = {'id': servicio.id,
                'nombre': servicio.nombre,
                'precio': servicio.precio}
        json.append(data)

    return JsonResponse(json, safe=False)


def obtener_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)

        data = {'id': servicio.id,
                'nombre': servicio.nombre,
                'descripcion': servicio.descripcion,
                'precio': servicio.precio}

        return JsonResponse(data)

    except ObjectDoesNotExist as e:
        return JsonResponse({})

