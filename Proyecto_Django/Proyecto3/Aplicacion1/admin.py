from django.contrib import admin
from Aplicacion1.models import *
from django.contrib.auth.models import Permission

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    list_display=("nombre", "seccion", "marca", "precio", "igv")
    search_fields=("seccion",)
    list_filter=("seccion",)
    readonly_fields=("marca",)
    
class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre", "email", "cumpleaños", "dias_restantes", "v_email", "inicial")

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Permission)