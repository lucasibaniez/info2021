from django import forms

from .models import Dvd, ESTADO_CHOICES

class DvdForm(forms.ModelForm):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

	estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
	class Meta:
		model = Dvd
		fields = ["nombre", "fecha_compra", "cant_unidades", "categorias", "estado"]

		



