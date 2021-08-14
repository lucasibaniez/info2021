from django.contrib.auth.models import User
from django.shortcuts           import render


def inicio(request):
	template_name="inicio.html"
	u = User.objects.get(username="lucas")
	u.last_name = "Suarez"
	u.save()
	return render(request,template_name)


def login(request):
	template_name="login.html"

	ctx={

	}
	return render(request,template_name, ctx )