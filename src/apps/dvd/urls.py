from django.urls import path 

from . import views

app_name = "dvd"

urlpatterns = [
	path('Nuevo/', views.CrearDvd.as_view(), name="nuevo"),
	path('Preguntar/', views.preguntar, name="preguntar"),
]