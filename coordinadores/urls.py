from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_coordinadores, name='listar-coordinadores'),
    path('modificar/<int:id>', views.modificar_coordinador, name='modificar-coordinador'),
    path('agregar/', views.agregar_coordinador, name='agregar-coordinador'),
    path('activar/<int:id>', views.activar_coordinador, name='activar-coordinador'),
    path('desactivar/<int:id>', views.desactivar_coordinador, name='desactivar-coordinador'),
]
    
