from django.urls import path
from . import views

urlpatterns = [
    path('modificar/<int:id>', views.actualizar_coordinador, name='modificar-coordinador')
]
