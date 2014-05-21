# -*- coding: utf-8 -*
from django import forms
from django.forms import ModelForm 
from models import *

class Formulario(forms.Form):
	"""docstring for Formulario"""
	nombre = forms.CharField(max_length=100)
	mensaje = forms.CharField(widget=forms.Textarea)
	mail = forms.EmailField()

class FormularioContacto(forms.Form):
	"""docstring for FormularioContacto"""
	correo = forms.EmailField()
	mensaje = forms.CharField()		

class Login(forms.Form):
	nick=forms.CharField(max_length=200)
	password=forms.CharField(widget=forms.PasswordInput)
	
class UsuarioForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=persona
		exclude=["fecha"]

class MaquinaForm(forms.ModelForm):
	class Meta:
		model=maquina

class ModalidadForm(forms.ModelForm):
	#lunes=forms.Date
	class Meta:
		model=modalidad



