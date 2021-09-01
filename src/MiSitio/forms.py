from django import forms 
from django.contrib.auth.forms import UserCreationForm

from apps.usuarios.models import Usuario

class RegistroForm(UserCreationForm):
	first_name = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={"placeholder":"ingrese su nombre", 'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

	class Meta:
		model = Usuario
		fields = ["first_name", "last_name"]
