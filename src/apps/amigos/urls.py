from django.urls import path 

from . import views

app_name = "amigos"

urlpatterns = [
	# path('Listar/', views.listar_amigos, name="listar"),
	path('Listar/', views.Listar.as_view(), name="listar"),
	# path('Nuevo/', views.nuevo_amigo, name="nuevo"),
	path('Nuevo/', views.CrearAmigo.as_view(), name="nuevo"),
	# path('Editar/<int:pk>/', views.editar_amigo, name="editar"),
	path('Editar/<int:pk>/', views.EditarAmigo.as_view(), name="editar")
] 