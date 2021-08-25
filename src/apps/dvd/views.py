from django.views.generic import ListView, CreateView
from django.shortcuts     import render
from django.urls          import reverse_lazy

from .models import Dvd
from .forms  import DvdForm, PreguntasForm, PreguntasForm2

class CrearDvd(CreateView):
	model = Dvd
	template_name = "dvd/crear.html"
	form_class = DvdForm 

	def get_success_url(self, **kwargs):
		return reverse_lazy("principal")

	def form_valid(self, form):
		"""
		f = form.save(commit=False)

		if f.estado == "I":
			pass
		"""
		return super(CrearDvd, self).form_valid(form)

# FormView
def preguntar2(request):
	template_name = "dvd/preguntar.html"

	ctx = {}

	if request.method == "POST":
		respuestas_marcadas = request.POST.getlist('respuestas')
		# string("asd")


	ctx["form"] = PreguntasForm(pregunta="¿Cual de los siguientes numeros son numeros pares?", respuestas=[(11, "44"),(12, "83"), (43, "91")])

	return render(request,template_name,ctx)

class Preg:
	def __init__(self, descripcion, lista_respuestas):
		self.descripcion=descripcion
		self.lista_respuestas=lista_respuestas

	def __str__(self):
		return self.descripcion
class Resp:
	def __init__(self, descripcion, es_correcta, id_resp):
		self.descripcion=descripcion
		self.es_correcta=es_correcta
		self.id_resp = id_resp




def preguntar(request):
	template_name = "dvd/preguntar.html"

	ctx = {}

	if request.method == "POST":
		# respuestas_marcadas = request.POST.getlist('respuestas')
		string("asd")
		#pass



	r11 = Resp(descripcion="asd", es_correcta=True, id_resp=1)
	r12 = Resp(descripcion="jjjjj", es_correcta=False, id_resp=2)
	r13 = Resp(descripcion="hhhhh", es_correcta=False, id_resp=3)
	x = [r11, r12, r13]
	
	p1 = Preg(descripcion="¿Como te va con tu proyecto final del info?", lista_respuestas=x)


	r21 = Resp(descripcion="gggg", es_correcta=True, id_resp=1)
	r22 = Resp(descripcion="dda", es_correcta=False, id_resp=2)
	r23 = Resp(descripcion="erq", es_correcta=False, id_resp=3)
	x = [r21, r22, r23]
	
	p2 = Preg(descripcion="¿Estas entendiendo como funcionan los formularios?", lista_respuestas=x)

	ctx["form"] = PreguntasForm2(preguntas=[p1, p2])

	return render(request,template_name,ctx)