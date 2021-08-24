from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Dvd
from .forms  import DvdForm

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