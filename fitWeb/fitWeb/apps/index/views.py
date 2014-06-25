#-*- coding: utf-8 -*
from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User, Group #importamos los modelos User y Group de django
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from models import *
from forms import *
import datetime
import json
from django.core.mail import EmailMessage
import pdb
import os
import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string

"""INDEX"""
def PaginaPrincipal(request):
	#preguntamos si el usuario inicio session
    if request.user.is_authenticated():
        if request.user.is_superuser:
        	return HttpResponseRedirect("/index_admin/")
        else:
        	return HttpResponseRedirect("/index_user/")
    else:
        if request.method=='POST':
            formulario=AuthenticationForm(request.POST)
            if formulario.is_valid:
                usuario=request.POST['username']
                contrasena=request.POST['password']
                acceso=authenticate(username=usuario,password=contrasena)
                if acceso is not None:
                    if acceso.is_active:
                        if acceso.is_superuser:
                        	login(request,acceso)
                        	return HttpResponseRedirect("/index_admin/")
                        else:
                        	login(request,acceso)
                        	return HttpResponseRedirect("/index_user/")
                    else:
                    	return HttpResponseRedirect("/noactivo/")
                else:
                    return HttpResponseRedirect("/nousuario/")
        else:
            formulario=AuthenticationForm()
        return render_to_response('index.html',{'formulario':formulario},RequestContext(request))

def nousuario(request):
	return render_to_response("nousuario.html",{},RequestContext(request))

def noactivo(request):
	return render_to_response("noactivo.html",{},RequestContext(request))

	"""ADMIN"""
def index_admin(request):
	return render_to_response("index_admin.html",{},RequestContext(request))

"""CLIENTES"""
def clientes(request):
	return render_to_response("cliente/clientes.html",{},RequestContext(request))

def registrar_usuario(request):
    if request.method=='POST':
        formulario=UserForm(request.POST)
        formulario2=fregistro(request.POST,request.FILES)
        if formulario.is_valid() and formulario2.is_valid():
        	usuario=request.POST['username']
        	formulario.save()     	
        	anio=request.POST['fecha_nacimiento_year']
        	mes=request.POST['fecha_nacimiento_month']
        	dia=request.POST['fecha_nacimiento_day']
        	fecha_nacimiento=anio+"-"+mes+"-"+dia
        	imagen=request.FILES['imagen']
        	sexo=request.POST['sexo']
        	ci=request.POST['ci']
        	telefono=request.POST['telefono']
        	nuevo_usuario=User.objects.get(username=usuario)
        	perfil=Persona.objects.create(user=nuevo_usuario,fecha_nacimiento=fecha_nacimiento,imagen=imagen,sexo=sexo,ci=ci,telefono=telefono)
       		error=False
       		mensaje="El cliente fue registrado"
       		return render_to_response('cliente/notificacion.html',{'error':error,'mensaje':mensaje},RequestContext(request))
    else:
    	formulario=UserForm()
        formulario2=fregistro()
    return render_to_response("cliente/registrar.html",{'formulario':formulario,'formulario2':formulario2},RequestContext(request))
	
def buscarCliente(request):
	if request.method=="POST":
		form=buscarForm(request.POST)
		if form.is_valid():
			busc=request.POST["buscar"]
			if busc!="":
				data=busc.split()
				lista=User.objects.filter(Q(first_name__contains=busc)|Q(last_name__contains=busc)|Q(username__contains=busc))
			return render_to_response("cliente/resultados.html",{"lista":lista},RequestContext(request))
	form=buscarForm()
	return render_to_response("cliente/buscarCliente.html",{"form":form},RequestContext(request))

def modificar_cliente(request,id):
	if request.method=='POST':
		usuario=User.objects.get(id=int(id))
		cliente=Persona.objects.get(user=usuario)
		formulario=fpersona(request.POST,request.FILES,instance=cliente)
		formulario2=fusuario(request.POST,instance=usuario)
		if formulario.is_valid():
			formulario.save()
			formulario2.save()
			return HttpResponseRedirect("/guardar/")
	else:
		usuario=User.objects.get(id=int(id))
		cliente=Persona.objects.get(user=usuario)
		formulario=fpersona(instance=cliente)
		formulario2=fusuario(instance=usuario)
	return render_to_response("cliente/modificar_registro.html",{'formulario':formulario,'formulario2':formulario2,'cliente':cliente},RequestContext(request))

def listarClientes(request):
	lista=list(Persona.objects.all())
	lista2=list(User.objects.all())
	return render_to_response("cliente/listarClientes.html",{"lista":lista,"lista2":lista2},RequestContext(request))

	"""PROFESIONALES"""
def profesionales(request):
	return render_to_response("profesional/profesionales.html",{},RequestContext(request))

def registrar_profesional(request):
	errorMsn=""
	if request.method=="POST":
		us=ProfesionalForm(request.POST,request.FILES)
		if us.is_valid():
			us.save()
			return HttpResponseRedirect('/profesional/profesionales/')
		else:
			errorMsn="Datos invalidos"
	us=ProfesionalForm()
	return render_to_response("profesional/registrar_profesional.html",{"usform":us,"error":errorMsn},RequestContext(request))

def modificar_profesional(request,id):
	prof=profesional.objects.get(id=id)
	if request.method=="POST":
		form=ProfesionalForm(request.POST,request.FILES,instance=prof)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/guardar/")
	else:
		form=ProfesionalForm(instance=prof)
	return render_to_response("profesional/modificar_profesional.html",{"form":form},RequestContext(request))
	
def buscar_profesional(request):
	if request.method=="POST":
		form=buscarForm(request.POST)
		if form.is_valid():
			criterio=request.POST["buscar"]
			if criterio!="":
				lista=profesional.objects.filter(Q(nombre__contains=criterio)|Q(apellidos__contains=criterio))
			return render_to_response("profesional/resultados_prof.html",{"lista":lista},RequestContext(request))
	form=buscarForm()
	return render_to_response("profesional/buscar_profesional.html",{"form":form},RequestContext(request))

def listar_profesionales(request):
	lista=list(profesional.objects.all())
	return render_to_response("profesional/listar_profesionales.html",{"lista":lista},RequestContext(request))	

	"""MAQUINAS"""
def maquinas(request):
	return render_to_response("maquina/maquinas.html",{},RequestContext(request))

def registrar_maquina(request):
	errorMsn=""
	if request.method=="POST":
		us=MaquinaForm(request.POST,request.FILES)
		if us.is_valid():
			us.save()
			return HttpResponseRedirect('/index_admin/')
		else:
			errorMsn="Datos invalidos"
	us=MaquinaForm()
	return render_to_response("maquina/registrar_maquina.html",{"usform":us,"error":errorMsn},RequestContext(request))

def modificar_maquina(request,id):
	maq=maquina.objects.get(id=id)
	if request.method=="POST":
		form=MaquinaForm(request.POST,request.FILES,instance=maq)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/guardar/")
	else:
		form=MaquinaForm(instance=maq)
	return render_to_response("maquina/modificar_maquina.html",{"form":form},RequestContext(request))	

def buscar_maquina(request):
	if request.method=="POST":
		form=buscarForm(request.POST)
		if form.is_valid():
			criterio=request.POST["buscar"]
			if criterio!="":
				lista=maquina.objects.filter(Q(nombre__contains=criterio))
			return render_to_response("maquina/resultados_maquina.html",{"lista":lista},RequestContext(request))
	form=buscarForm()
	return render_to_response("maquina/buscar_maquina.html",{"form":form},RequestContext(request))

def listar_maquinas(request):
	lista=list(maquina.objects.all())
	return render_to_response("maquina/listar_maquinas.html",{"lista":lista},RequestContext(request))	

	"""MODALIDADES"""
def modalidades(request):
	return render_to_response("modalidad/modalidades.html",{},RequestContext(request))

def registrar_modalidad(request):
	errorMsn=""
	if request.method=="POST":
		us=ModalidadForm(request.POST)
		if us.is_valid():
			us.save()
			return HttpResponseRedirect('/guardar/')
		else:
			errorMsn="Datos invalidos"
	us=ModalidadForm()
	return render_to_response("modalidad/registrar_modalidad.html",{"usform":us,"error":errorMsn},RequestContext(request))

def modificar_modalidad(request,id):
	mod=modalidad.objects.get(id=id)
	if request.method=="POST":
		form=ModalidadForm(request.POST,instance=mod)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/guardar/")
	else:
		form=ModalidadForm(instance=mod)
	return render_to_response("modalidad/modificar_modalidad.html",{"form":form},RequestContext(request))	

def buscar_modalidad(request):
	if request.method=="POST":
		form=buscarForm(request.POST)
		if form.is_valid():
			criterio=request.POST["buscar"]
			if criterio!="":
				lista=modalidad.objects.filter(Q(nombre__contains=criterio))
			return render_to_response("modalidad/resultados_modalidad.html",{"lista":lista},RequestContext(request))
	form=buscarForm()
	return render_to_response("modalidad/buscar_modalidad.html",{"form":form},RequestContext(request))

def listar_modalidades(request):
	lista=list(modalidad.objects.all())
	return render_to_response("modalidad/listar_modalidades.html",{"lista":lista},RequestContext(request))	

"""ALIMENTOS"""
def alimentos_view(request):
	return render_to_response("alimento/alimentos.html",{},RequestContext(request))

def registrar_alimento(request):
	errorMsn=""
	if request.method=="POST":
		us=AlimentosForm(request.POST,request.FILES)
		if us.is_valid():
			us.save()
			return HttpResponseRedirect('/guardar/')
		else:
			errorMsn="Datos invalidos"
	us=AlimentosForm()
	return render_to_response("alimento/registrar_alimento.html",{"usform":us,"error":errorMsn},RequestContext(request))

def modificar_alimento(request,id):
	alim=alimentos.objects.get(id=id)
	if request.method=="POST":
		form=AlimentosForm(request.POST,request.FILES,instance=alim)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/guardar/")
	else:
		form=AlimentosForm(instance=alim)
	return render_to_response("alimento/modificar_alimento.html",{"form":form},RequestContext(request))	

def buscar_alimento(request):
	if request.method=="POST":
		form=buscarForm(request.POST)
		if form.is_valid():
			criterio=request.POST["buscar"]
			if criterio!="":
				lista=alimentos.objects.filter(Q(nombre__contains=criterio))
			return render_to_response("alimento/resultados_alimento.html",{"lista":lista},RequestContext(request))
	form=buscarForm()
	return render_to_response("alimento/buscar_alimento.html",{"form":form},RequestContext(request))

def listar_alimentos(request):
	lista=list(alimentos.objects.all())
	return render_to_response("alimento/listar_alimentos.html",{"lista":lista},RequestContext(request))	

"""DIETAS"""
def dietas_view(request):
	return render_to_response("dietas/dietas.html",{},RequestContext(request))

def registrar_dieta(request):
	errorMsn=""
	if request.method=="POST":
		us=DietasForm(request.POST,request.FILES)
		if us.is_valid():
			us.save()
			return HttpResponseRedirect('/guardar/')
		else:
			errorMsn="Datos invalidos"
	us=DietasForm()
	return render_to_response("dietas/registrar_dieta.html",{"usform":us,"error":errorMsn},RequestContext(request))

def modificar_dieta(request,id):
	diet=dietas.objects.get(id=id)
	if request.method=="POST":
		form=DietasForm(request.POST,request.FILES,instance=diet)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/guardar/")
	else:
		form=DietasForm(instance=diet)
	return render_to_response("dietas/modificar_dieta.html",{"form":form},RequestContext(request))
	
def buscar_dieta(request):
	if request.method=="POST":
		form=buscarForm(request.POST)
		if form.is_valid():
			criterio=request.POST["buscar"]
			if criterio!="":
				lista=dietas.objects.filter(Q(nombre__contains=criterio))
			return render_to_response("dietas/resultados_dieta.html",{"lista":lista},RequestContext(request))
	form=buscarForm()
	return render_to_response("dietas/buscar_dieta.html",{"form":form},RequestContext(request))

def listar_dietas(request):
	lista=list(dietas.objects.all())
	return render_to_response("dietas/listar_dietas.html",{"lista":lista},RequestContext(request))	

"""REPORTES"""
def reportes_view(request):
	return render_to_response("reporte/reportes.html",{},RequestContext(request))

def generar_pdf(html):
	resultado=StringIO.StringIO()
	pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(),mimetype='application/pdf')
	return HttpResponse("Error en generar el pdf")

def crear_reporte_clientes(request):
	usuario=User.objects.all()
	html=render_to_string("reporte/reporte_clientes.html",{'pagesize':'A4','usuario':usuario},RequestContext(request))
	return generar_pdf(html)

def crear_reporte_profesionales(request):
	profes=profesional.objects.all()
	html=render_to_string("reporte/reporte_profesionales.html",{'pagesize':'A4','profes':profes},RequestContext(request))
	return generar_pdf(html)

	"""USER"""
def index_user(request):
	usuario=request.user
	persona=Persona.objects.get(user=usuario)
	return render_to_response("index_user.html",{'persona':persona},RequestContext(request))

def mostrar_usuario(request,id):
    usuario=User.objects.get(id=int(id))
    context = {
        'usuario'  : usuario,
        'nombre' : usuario.get_full_name(),
        'perfil' : usuario.get_profile(),
        }
    return render_to_response("cliente_usuario/usuario_perfil.html",context,RequestContext(request))

def calculadoras(request):
	return render_to_response("cliente_usuario/calculadoras.html",{},RequestContext(request))

def calculadora2(request):
    if request.method=="POST":
        formulario=calculadoraForm2(request.POST)
        usuario=request.user
        nuevo_usuario=User.objects.get(username=usuario)
        cliente=Persona.objects.get(user=nuevo_usuario)
        if formulario.is_valid():
            sexo=cliente.sexo
            peso=request.POST["peso"]
            estatura=request.POST["estatura"]
            edad=request.POST["edad"]
            actividad=request.POST["actividad"]
            if sexo == '1':
                tmb = 66 + (13.7 * float(peso)) +(5 * float(estatura)) - (6.8 * float(edad))
            else:
                tmb = 655 + (9.6 * float(peso)) + (1.8 * float(estatura)) - (4.7 * float(edad))
            if actividad=='Sedentario':
                ccd = tmb * 1.2
            if actividad=="Actividad ligera":
                ccd = tmb * 1.375
            if actividad=='Actividad moderada':
                ccd = tmb * 1.55
            if actividad=='Actividad intensa':
                ccd = tmb * 1.725
            if actividad=='Actividad muy intensa':
                ccd = tmb * 1.9
            return HttpResponse(str("metabolismo basal: ")+str(tmb)+str(" Calorias necesarias para mantener el peso: ")+str(ccd))
    else:
        formulario=calculadoraForm2()
    return render_to_response("calculadors/calculadora_harris_benedict.html",{'formulario':formulario},RequestContext(request))

def guardar(request):
	return render_to_response("guardar.html",{},RequestContext(request))

def notificacion(request):
	return render_to_response("notificacion.html",{},RequestContext(request))

def salir(request):
	logout(request)
	return HttpResponseRedirect('/')
	
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

def verificar(request):
    if request.method=='POST':
        usuario=request.POST['username']
        try:
            u=User.objects.get(username=usuario)
            return HttpResponse("El usuario ya existe, cambie otro")
        except User.DoesNotExist:
            return HttpResponse("")
    else:
        return HttpResponse()
