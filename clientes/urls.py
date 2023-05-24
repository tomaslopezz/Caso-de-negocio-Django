from django.urls import path
from . import views

urlpatterns = [
    path('activar/<int:id>', views.activar_cliente)
]
