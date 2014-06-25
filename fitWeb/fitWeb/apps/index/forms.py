# -*- coding: utf-8 -*
from django.forms import ModelForm 
from django.forms.extras.widgets import *
from django.contrib.auth.models import User
from django import forms
from models import *
from django.contrib.auth.forms import UserCreationForm


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

class UserForm(UserCreationForm):
    first_name=forms.CharField(max_length=20,required=True,label="Nombre")
    last_name=forms.CharField(max_length=30,required=True,label="Apellidos")
    email=forms.EmailField(required=True,widget=forms.TextInput)
    class Meta:
        model=User
        fields=("username","password1","password2","first_name","last_name","is_active","email")
    def save(self, commit=True):
        user=super(UserForm,self).save(commit=False)
        user.first_name=self.cleaned_data.get("first_name")
        user.last_name=self.cleaned_data.get("last_name")
        user.email=self.cleaned_data.get("email")
        if commit:
            user.save()
        return user

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

class calculadoraForm2(ModelForm):
	class Meta:
		model=Calculadora2
		exclude = ['persona']

class ProfesionalForm(forms.ModelForm):
	estado=forms.ChoiceField(widget=forms.RadioSelect, choices=ESTADO)
	class Meta:
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


