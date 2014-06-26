from django.conf.urls import patterns, include, url

from django.conf import settings
#from django.contrib import admin
from fitWeb.apps.index.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',PaginaPrincipal),

    url(r'^nousuario/',nousuario),
    url(r'^noactivo/',noactivo),
    url(r'^verificar/usuario/$',verificar),
    
    url(r'^index_admin/$',index_admin),

    url(r'^cliente/clientes/$',clientes),
    url(r'^cliente/registrar/$',registrar_usuario),
    url(r'^cliente/buscarCliente/$',buscarCliente),
    url(r'^cliente/modificar/(?P<id>\d+)/$',modificar_cliente),
    #url(r'^cliente/eliminar/(?P<id>\d+)/$',eliminar_cliente),
    url(r'^cliente/listarClientes/$',listarClientes),
    url(r'^cliente/notificacion/$',notificacion),

    url(r'^profesional/profesionales/',profesionales),
    url(r'^profesional/registrar_profesional/',registrar_profesional),
    url(r'^profesional/buscar_profesional/',buscar_profesional),
    url(r'^profesional/modificar_profesional/(?P<id>\d+)/$',modificar_profesional),
    url(r'^profesional/listar_profesionales/',listar_profesionales),

    url(r'^maquina/maquinas/',maquinas),
    url(r'^maquina/registrar_maquina/',registrar_maquina),
    url(r'^maquina/buscar_maquina/',buscar_maquina),
    url(r'^maquina/modificar_maquina/(?P<id>\d+)/$',modificar_maquina),
    url(r'^maquina/listar_maquinas/',listar_maquinas),

    url(r'^modalidad/modalidades/',modalidades),
    url(r'^modalidad/registrar_modalidad/',registrar_modalidad),
    url(r'^modalidad/buscar_modalidad/',buscar_modalidad),
    url(r'^modalidad/modificar_modalidad/(?P<id>\d+)/$',modificar_modalidad),
    url(r'^modalidad/listar_modalidades/',listar_modalidades),

    url(r'^alimento/alimentos/',alimentos_view),
    url(r'^alimento/registrar_alimento/',registrar_alimento),
    url(r'^alimento/buscar_alimento/',buscar_alimento),
    url(r'^alimento/modificar_alimento/(?P<id>\d+)/$',modificar_alimento),
    url(r'^alimento/listar_alimentos/',listar_alimentos),

    url(r'^dietas/dietas/',dietas_view),
    url(r'^dietas/registrar_dieta/',registrar_dieta),
    url(r'^dietas/buscar_dieta/',buscar_dieta),
    url(r'^dietas/modificar_dieta/(?P<id>\d+)/$',modificar_dieta),
    url(r'^dietas/listar_dietas/',listar_dietas),

    url(r'^reporte/reportes/',reportes_view), 
    url(r'^reporte/reporte_clientes/',crear_reporte_clientes),    
    url(r'^reporte/reporte_profesionales/',crear_reporte_profesionales),    

    url(r'^index_user/$',index_user),
    #url(r'^index_user/(?P<id>\d+)/$',index_user),
    #url(r'^mi_perfil/(?P<nombre>.*)/','mi_perfil'),
    url(r'^index/(\d+)/$',mostrar_usuario),
    url(r'^cliente_usuario/calculadoras/$',calculadoras),
    url(r'^calculadors/calculadora_harris_benedict/$',calculadora2),
    
    url(r'^blog/$',blog),
    url(r'^login/$',login),
    url(r'^salir/$',salir), 
    
    url(r'^contacto/$',contacto),
    url(r'^guardar/',guardar),
    url(r'^gracias/',gracias),
    url(r'^contacto_email/$',contacto_email),
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    #url(r'^tinymce/', include('tinymce.urls')),

)
