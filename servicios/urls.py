from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_servicios, name='listar-servicios'),
    path('agregar/', views.agregar_servicio, name='agregar-servicio'),
    path('modificar/<int:id>', views.modificar_servicio, name='modificar-servicio'),
    path('activar/<int:id>', views.activar_servicio, name='activar-servicio'),
    path('desactivar/<int:id>', views.desactivar_servicio, name='desactivar-servicio')
]
