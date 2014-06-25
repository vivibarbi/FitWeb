# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import *
#from tinymce.models import HTMLField
from PIL import *
from django.contrib.auth.models import User
from thumbs import ImageWithThumbsField

ESTADO_VISIBLE = [1,2]

# Create your models here.
class Persona(models.Model):
    user = models.ForeignKey(User, unique=True)
    fecha_nacimiento=models.DateField()
    imagen =ImageWithThumbsField(null=True,sizes=((120,120),(48,48)),upload_to='img_usuario')
    sexo = models.IntegerField(null=False)
    ci=models.IntegerField(null=False,unique=True)
    telefono = models.IntegerField(null=True,max_length=8)

class profesional(models.Model):
	"""docstring for profesinal"""
	nombre = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	imagen =models.ImageField(null=True,upload_to='img_profesional')
	ci = models.IntegerField(max_length=8)
	direccion = models.CharField(max_length=200)
	telefono = models.IntegerField(max_length=7)
	email = models.EmailField(max_length=80)
	estado = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.nombre;

class maquina(models.Model):
	"""docstring for maquina"""
	nombre = models.CharField(max_length=200)
	tipo = models.CharField(max_length=50)
	imagen = models.ImageField(null=True,upload_to='img_maquina')
	descripcion = models.TextField()
	
	def __unicode__(self):
		return self.nombre;

class modalidad(models.Model):
	"""docstring for modalidad"""
	nombre = models.CharField(max_length=100)
	nombre_instructor = models.ManyToManyField(profesional)
	costo_sesion = models.IntegerField(max_length=10)
	costo_mensual = models.IntegerField(max_length=10)
	descripcion = models.TextField()
	
	def __unicode__(self):
		return self.nombre;

class alimentos(models.Model):
	"""docstring for alimentos"""
	nombre = models.CharField(max_length=100)
	peso = models.IntegerField(max_length=10)
	calorias = models.IntegerField(max_length=10)
	imagen = models.ImageField(null=True, upload_to='img_alimento')
	descripcion = models.TextField()
	
	def __unicode__(self):
		return self.nombre;

class dietas(models.Model):
	"""docstring for dietas"""
	nombre = models.CharField(max_length=100)
	imagen = models.ImageField(null=True,upload_to='img_dieta')
	descripcion = models.TextField()
	def __unicode__(self):
		return self.nombre;

class Calculadora2(models.Model):	
	peso = models.FloatField(null=False)
	estatura = models.FloatField(null=False)
	edad = models.IntegerField(null=False)
	actividad = models.CharField(null=False,max_length=30)
	persona = models.ForeignKey(Persona)

class ManejadorPost(models.Manager):
	def get_query_set(self):
		default_queryset = super(ManejadorPost,self).get_query_set()
		return default_queryset.filter(status__in=ESTADO_VISIBLE)

class Categorias(models.Model):
	"""docstring for Categorias"""
	nombre = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True, help_text='Esto es para URL')
	descripcion = models.TextField()
	creada_en = models.DateTimeField(auto_now_add=True)
	actualizada_al = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'categorias'
		ordering = ['creada_en']
		verbose_name_plural = 'Categorias'
	def __unicode__(self):
		return self.nombre

class BlogPost(models.Model):
	"""docstring for Informacion"""
	ESTADOS=( (1,'Publicado'),(2,'Archivado'),(3,'Necesita editarse'),(4,'Necesita aprovacion') )
	status = models.IntegerField(choices=ESTADOS,default=4)
	objetos_panel = models.Manager() 
	objects = ManejadorPost()
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User)
	#slug = models.SlugField()
	time = models.DateTimeField() #(auto_now_add=True)
	categorias_post = models.ManyToManyField(Categorias)
	#imagen = models.ImageField(upload_to='photos')
	#body = HTMLField()
	body = models.TextField()

	class Meta:
		db_table = 'entradas'
		ordering = ['-time']
		verbose_name_plural = 'Post'
				
	def __unicode__(self):
		return self.title

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'time', 'status')
	list_instances = True
	#search_fields = ['title']

class CategoriasAdmin(admin.ModelAdmin):
	"""docstring for CategoriasAdmin"""
	list_display = ('nombre', 'creada_en', 'actualizada_al')
	list_display_links = ('nombre','creada_en','actualizada_al')
	list_per_page = 20
	ordering = ['nombre']
	search_fields= ['nombre','descripcion']

prepopulated_fields = {'slug' : ('nombre',)} 
	
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Categorias,CategoriasAdmin)
admin.site.register(Persona)
admin.site.register(profesional)
admin.site.register(maquina)
admin.site.register(modalidad)
admin.site.register(alimentos)
admin.site.register(dietas)

