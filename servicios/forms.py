from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'precio':'Precio',
            'activo':'Activo'
        }