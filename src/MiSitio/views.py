from django.contrib.auth.models import User
from django.shortcuts           import render

from apps.dvd.models import Categoria

def inicio(request):
	template_name="inicio.html"
	return render(request,template_name)