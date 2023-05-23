from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'activo')
    search_fields = ('nombre', 'apellido')
    list_filter = ('activo',)

admin.site.register(Cliente, ClienteAdmin)
