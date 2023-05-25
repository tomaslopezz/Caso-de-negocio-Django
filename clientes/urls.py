from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_clientes, name='listar-clientes'),
    path('agregar/', views.agregar_cliente, name='agregar-cliente'),
    path('activar/<int:id>', views.activar_cliente, name='activar-cliente')
]

