from django.shortcuts import render
from .models import Coordinador

# Create your views here.
def listar_coordinadores(request):
    coordinadores = Coordinador.objects.all()
    context = {'coordinadores':coordinadores}

    return render(request,'listado', context)

