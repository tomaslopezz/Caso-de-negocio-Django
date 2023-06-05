from django.contrib import admin
from .models import Reserva


# Register your models here.
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('fecha_reserva', 'fecha_servicio', 'cliente',
                    'servicio', 'empleado', 'coordinador')
    search_fields = ('cliente', 'empleado', 'coordinador', 'servicio')


admin.site.register(Reserva, ReservaAdmin)
