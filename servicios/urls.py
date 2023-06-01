from django.urls import path
from . import views

urlpatterns = [
    path('activar/<int:id>', views.activar_servicio, name='activar-servicio'),
    path('modficar/<int:id>', views.modificar_servicio, name='modificar-servicio')
]