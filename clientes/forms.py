from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        fields = ('nombre', 'apellido')
        labels = {'nombre':'Nombre',
                  'apellido':'Apellido'
                }