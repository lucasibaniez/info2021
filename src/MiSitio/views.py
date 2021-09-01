from django.contrib.auth.models import User
from django.shortcuts           import render

from apps.dvd.models import Categoria

from .forms import RegistroForm

def inicio(request):
	template_name="inicio.html"
	return render(request,template_name)



def registro(request):
	template_name="registro.html"
	ctx = {"form": RegistroForm()}
	return render(request,template_name, ctx)