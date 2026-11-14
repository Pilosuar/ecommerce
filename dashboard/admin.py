from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'stock', 'creado_en')
    search_fields = ('nombre', 'categoria')
    list_filter = ('categoria',)
