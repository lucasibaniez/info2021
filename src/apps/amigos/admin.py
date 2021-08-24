from django.contrib import admin

from .models import Amigo, Telefono 


class AmigosAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'domicilio']

admin.site.register(Amigo, AmigosAdmin)

class TelefonoAdmin(admin.ModelAdmin):
	list_display = ['id', 'amigo', 'codigo_area', 'codigo_celular', 'numero']

admin.site.register(Telefono, TelefonoAdmin)