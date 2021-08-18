from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy

from .models import Amigo
from .forms  import AmigoForm
"""
@login_required
def listar_amigos(request):
	template_name="amigos/listar.html"
	
	lista_de_amigos = Amigo.objects.filter(nombre='Lucas')
	
	ctx={
		'amigos': lista_de_amigos
	}
	return render(request,template_name, ctx )


def nuevo_amigo(request):
	template_name="amigos/nuevo.html"

	if request.method == "POST":
		nombre = request.POST.get("nombre", None)
		domicilio = request.POST.get("domicilio", None)
		apellido = request.POST.get("apellido", None)
		a = Amigo.objects.create(nombre=nombre, apellido=apellido, domicilio=domicilio)

		return redirect('amigos:listar')

	ctx={
		'form': AmigoForm()
	}
	return render(request,template_name, ctx )


def editar_amigo(request, pk):
	template_name="amigos/editar.html"
	ctx = {
		'amigo': Amigo.objects.get(id=pk)
	}
	return render(request,template_name, ctx )

"""

class EditarAmigo(UpdateView):
	model = Amigo
	template_name = "amigos/editar.html"
	form_class = AmigoForm 

	def get_success_url(self, **kwargs):
		return reverse_lazy("amigos:listar")

class CrearAmigo(CreateView):
	model = Amigo
	template_name = "amigos/nuevo.html"
	form_class = AmigoForm 

	def get_success_url(self, **kwargs):
		return reverse_lazy("amigos:listar")

class Listar(LoginRequiredMixin, ListView):
	template_name = "amigos/listar.html"
	model = Amigo
	context_object_name = 'amigos'

	
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Amigo.objects.all()

		return Amigo.objects.filter(nombre="Lucas")
	

	"""
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["color"] = "amarillo"
		return context
	"""