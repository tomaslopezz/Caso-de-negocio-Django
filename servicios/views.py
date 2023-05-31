from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from .models import Servicio


# Create your views here.

def activar_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = True
        servicio.save()
        return HttpResponse("<h1>Servicio activado con exito</h1>")
    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Servicio inexistente</h1>")
