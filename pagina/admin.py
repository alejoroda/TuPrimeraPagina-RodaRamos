from django.contrib import admin

from .models import Cliente, Producto, Compra, Categoria, Comentario, Respuesta, Perfil

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):   
    list_display = ("nombre", "correo")
    search_fields = ("nombre", "correo")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "fechapublicacion", "autor", "estado")
    list_filter = ("estado", "fechapublicacion", "autor")
    search_fields = ("nombre", "autor__username")
    date_hierarchy = "fechapublicacion"
    ordering = ("-fechapublicacion",)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("cliente", "producto", "cantidad", "fecha")
    list_filter = ("fecha", "producto")
    search_fields = ("cliente__nombre", "producto__nombre")
    date_hierarchy = "fecha"
    ordering = ("-fecha",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("categoria",)
    search_fields = ("categoria",)

admin.site.register(Comentario)
admin.site.register(Respuesta)
admin.site.register(Perfil)
