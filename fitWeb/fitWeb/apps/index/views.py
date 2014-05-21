# -*- coding: utf-8 -*
from django.shortcuts import render,render_to_response
from django.template import RequestContext, loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from models import *
from forms import *
import datetime
from django.core.mail import EmailMessage

def PaginaPrincipal(request):
	errorMsn=""
	if request.method=="POST":
		log=Login(request.POST)
		if log.is_valid():
			data=log.cleaned_data
			s=persona.objects.filter(nick=data["nick"],password=data["password"])
			usuarios=request.POST['nick']			
			pw=request.POST['password']
			u=persona.objects.get(nick=usuarios,password=pw)
			if (len(s)>0):
				#s=persona.objects.filter(tipo=data["tipo"])
				#### redireccionar ###
				if u.tipo=='admin':
					return HttpResponseRedirect("/index_admin/")
				else:
					return HttpResponseRedirect("/index_user/")
			else:
				#errorMsn="nombre de usuario incorrecto"
				return render_to_response('nousuario.html',{},RequestContext(request))
		else:
			errorMsn="datos invalidos"
	login=Login()

	if request.method == 'POST':
		form = Formulario(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/fitWeb/apps/gracias/')
	else:
		form = Formulario()

	return render_to_response("index.html",{"login":login,"error":errorMsn,"form":form},RequestContext(request))

def index_admin(request):
	return render_to_response("index_admin.html",{},RequestContext(request))

def index_user(request):
	return render_to_response("index_user.html",{},RequestContext(request))

def login(request):
	errorMsn=""
	if request.method=="POST":
		log=Login(request.POST)
		if log.is_valid():
			data=log.cleaned_data
			s=persona.objects.filter(nick=data["nick"],password=data["password"])
			if (len(s)>0):
				return HttpResponseRedirect("/../")
			else:
				errorMsn="nombre de usuario incorrecto"
		else:
			errorMsn="datos invalidos"
	login=Login()
	return render_to_response("login.html",{"login":login,"error":errorMsn},RequestContext(request))

def registrar(request):
	errorMsn=""
	if request.method=="POST":
		us=UsuarioForm(request.POST)
		p=us.save(commit=False)
		p.fecha=datetime.datetime.now().date()
		if us.is_valid():
			us.save()
			#errorMsn="Datos guardados"
			return HttpResponseRedirect('/fitWeb/apps/guardar/')
		else:
			errorMsn="Datos invalidos"
	us=UsuarioForm()
	return render_to_response("registrar.html",{"usform":us,"error":errorMsn},RequestContext(request))

def registrar_maquina(request):
	errorMsn=""
	if request.method=="POST":
		us=MaquinaForm(request.POST)
		if us.is_valid():
			us.save()
			return HttpResponseRedirect('/index_admin/')
		else:
			errorMsn="Datos invalidos"
	us=MaquinaForm()
	return render_to_response("registrar_maquina.html",{"usform":us,"error":errorMsn},RequestContext(request))

def registrar_modalidad(request):
	errorMsn=""
	if request.method=="POST":
		us=ModalidadForm(request.POST)
		if us.is_valid():
			us.save()
			return HttpResponseRedirect('/index_admin/')
		else:
			errorMsn="Datos invalidos"
	us=ModalidadForm()
	return render_to_response("registrar_modalidad.html",{"usform":us,"error":errorMsn},RequestContext(request))

def guardar(request):
	html='<html><body>"Usuario registrado.. <br><br><a href="/index_admin/">Atras</a></body></html>"'
	return HttpResponse(html)

def blog(request):
	posts = BlogPost.objects.all()
	return render_to_response("blog.html",{'posts':posts},RequestContext(request))	
	#mi_template = loader.get_template("blog.html")
	#mi_contexto = Context({'posts':posts})
	#return HttpResponse(mi_template(mi_contexto))

def contacto(request):
	if request.method == 'POST':
		form = Formulario(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/fitWeb/apps/gracias/')
	else:
		form = Formulario()
	return render_to_response("contacto.html",{'form':form},RequestContext(request))

def gracias(request):
	html='<html><body>"Gracias por enviar su commentario...</body></html>"'
	return HttpResponse(html)

def contacto_email(request):
	if request.method == 'POST':
		formulario = FormularioContacto(request.POST)
		if formulario.is_valid():
			asunto = 'Este es un mensaje de mi blog FITWEB'
			mensaje = formulario.cleaned_data['mensaje']
			mail = EmailMessage(asunto, mensaje, to=['viviana_kitty@ymail.com'])
			mail.send()
		return HttpResponseRedirect('/')
	else:
		formulario = FormularioContacto()
	return render_to_response("contacto_email.html",{'formulario':formulario},RequestContext(request))



