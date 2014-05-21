from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
from fitWeb.apps.index.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fitWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',PaginaPrincipal),
    url(r'^index_admin/',index_admin),
    url(r'^index_user/',index_user),
    url(r'^blog/$',blog),
    url(r'^login/$',login),
    url(r'^registrar/',registrar),
    url(r'^registrar_maquina/',registrar_maquina),
    url(r'^registrar_modalidad/',registrar_modalidad),
    url(r'^contacto/$',contacto),
    url(r'^guardar/',guardar),
    url(r'^gracias/',gracias),
    url(r'^contacto_email/$',contacto_email),

    #url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^media/(?P<path>.*)$','django.views.static.server',{'document_root':settings.MEDIA_ROOT,}),
)
