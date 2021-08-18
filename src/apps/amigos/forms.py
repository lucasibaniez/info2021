from django import forms

from .models import Amigo

class AmigoForm(forms.ModelForm):
	class Meta:
		model = Amigo
		fields = ["nombre", "domicilio", "apellido"]