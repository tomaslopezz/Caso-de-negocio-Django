from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reserva


# Create your views here.
def eliminar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.delete()
        return HttpResponse("<h1>Reserva eliminada con exito</h1>")
    except ObjectDoesNotExist as e:
        return HttpResponse("<h1>Reserva inexistente</h1>")
