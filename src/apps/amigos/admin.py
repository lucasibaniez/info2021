from django.contrib import admin

from .models import Amigo 


class AmigosAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'domicilio']


admin.site.register(Amigo, AmigosAdmin)