# -*- coding: utf-8 -*
from django.forms import ModelForm 
from django.forms.extras.widgets import *
from django.contrib.auth.models import User
from django import forms
from models import *

ESTADO=(('1','Habilitado',),('2','Dado_baja',))
lista_anios = range(2013,1905,-1)
SEXO = (('1','Hombre',),('2','Mujer',))

class fpersona(forms.ModelForm):
	class Meta():
		model=Persona
		exclude=['user','sexo']

class fusuario(forms.ModelForm):
	class Meta():
		model=User
		exclude=['last_login','password','is_superuser','is_staff','date_joined','groups','user_permissions']

class fregistro(forms.ModelForm):
    fecha_nacimiento=forms.DateField(widget=SelectDateWidget(years=lista_anios))
    sexo=forms.ChoiceField(widget=forms.RadioSelect, choices=SEXO)
    class Meta:
    	model=Persona
    	exclude = ['user']

"""class fregistro2(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(widget=forms.PasswordInput,help_text='confirmacion de contraseña',label='Password2')
	class Meta():
		model=User
		exclude=['is_superuser','last_login','is_staff','date_joined','groups','user_permissions']
"""
class ProfesionalForm(forms.ModelForm):
	estado=forms.ChoiceField(widget=forms.RadioSelect, choices=ESTADO)
	class Meta():
		model=profesional

class MaquinaForm(forms.ModelForm):
	class Meta:
		model=maquina

class ModalidadForm(forms.ModelForm):
	class Meta:
		model=modalidad

class AlimentosForm(forms.ModelForm):
	class Meta:
		model=alimentos

class DietasForm(forms.ModelForm):
	class Meta:
		model=dietas

class buscarForm(forms.Form):
	buscar=forms.CharField(max_length=200)

class Login(forms.Form):
	nick=forms.CharField(max_length=200)
	password=forms.CharField(widget=forms.PasswordInput)
	
class Formulario(forms.Form):
	"""docstring for Formulario"""
	nombre = forms.CharField(max_length=100)
	mensaje = forms.CharField(widget=forms.Textarea)
	mail = forms.EmailField()

class FormularioContacto(forms.Form):
	"""docstring for FormularioContacto"""
	correo = forms.EmailField()
	mensaje = forms.CharField()		


