from django.urls import path 

from . import views

app_name = "amigos"

urlpatterns = [
	path('Listar/', views.listar_amigos)
] 