from django.contrib import admin
from .models import Servicio


# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'activo')
    search_fields = ('nombre',)
    list_filter = ('activo',)


admin.register(Servicio, ServicioAdmin)
