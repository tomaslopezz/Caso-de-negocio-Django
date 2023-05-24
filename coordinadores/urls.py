from django.urls import path
from . import views

urlpatterns = [
    path('listado', views.listar_coordinadores, name='listar-coordinadores'),
    path('modificar/<int:id>', views.actualizar_coordinador, name='modificar-coordinador'),
    path('nuevo', views.registrar_coordinador, name='registrar-coordinador'),
    path('desactivar/<int:id>', views.desactivar_coordinador, name='desactivar-coordinador'),
]
    
