from django.contrib import admin

from .models import Categoria , Dvd

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre']

admin.site.register(Categoria, CategoriaAdmin)

class DvdAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'fecha_compra', 'cant_unidades']

admin.site.register(Dvd, DvdAdmin)