from django.forms import ModelForm
from django import forms
from principal.models import Trabajador, Cafe

class TrabajadorForm(ModelForm):
	class Meta:
		model = Trabajador