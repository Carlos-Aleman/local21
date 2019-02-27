from django import forms

from .models import Jugador
from .models import Equipo
from .models import Estadio

class FormJugador(forms.ModelForm):
	content = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	apellido = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	edad = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	estatura = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	nacioalidad = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	equipo = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	universidad = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	posicion = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	
	class Meta:
		model = Jugador
		fields = [
	
		"content",
		"apellido",
		"edad",
		"estatura",
		"nacionalidad",
		"equipo",
		"universidad",
		"posicion",
		
		]


class FormEquipo(forms.ModelForm):
	content = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	liga = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	estado = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	campionatos = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	
	class Meta:
		model = Equipo
		fields = [
	
		"content",
		"liga",
		"estado",
		"campionatos",
		
		]


class FormEstadio(forms.ModelForm):
	content = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	ubicacion = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	capacidad = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	equipo_local = forms.CharField(widget=forms.TextInput(attrs={"class": "form form-control"}))
	
	class Meta:
		model = Estadio
		fields = [
	
		"content",
		"ubicacion",
		"capacidad",
		"equipo_local",
		
		]

