from django.urls import path
from django.conf.urls import url

from . import views

app_name = "dvd"

urlpatterns = [
	path('Listar/', views.Listar.as_view(), name="listar"),
	path('Nuevo/', views.CrearDvd.as_view(), name="nuevo"),
	path('Preguntar/', views.preguntar, name="preguntar"),

	# path('Jugar/Nivel/<int:nivel>/', views.Jugar, name="jugar"),
	# url(r'^Jugar/Nivel/(?P<nivel>[0-9]+)$')
]