from django.urls import path
from . import views

urlpatterns = [
    path('servicios/', views.listar_servicios, name='listar-servicios'),
    path('servicios/<int:id>', views.obtener_servicio, name='obtener-servicio'),
    path('coordinadores/', views.listar_coordinadores, name='listar-coordinadores')
]
