from django import forms

from .models import Amigo

class AmigoForm(forms.ModelForm):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	domicilio = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	apellido = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Amigo
		fields = ["nombre", "domicilio", "apellido"]

	def clean_nombre(self):
		nombre = self.cleaned_data["nombre"]

		if len(nombre)<3:
			self.add_error("nombre", "La longitud del nombre deber ser mayor a 3")

		return nombre