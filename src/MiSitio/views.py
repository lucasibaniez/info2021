from django.shortcuts import render

def inicio(request):
	template_name="inicio.html"

	lista_alumnos = [
		"alumno 1",
		"alumno 2"
	]

	ctx={
		'username': "lucas",
		"lista": lista_alumnos
	}
	return render(request,template_name, ctx )

def login(request):
	template_name="login.html"

	ctx={

	}
	return render(request,template_name, ctx )