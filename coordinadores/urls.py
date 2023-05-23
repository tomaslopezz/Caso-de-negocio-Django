from django.urls import path
from . import views

urlpatterns = [
    path('listado', views.listar_coordinadores, name='listar-coordinadores'),
]