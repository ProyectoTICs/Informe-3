from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto_cafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','principal.views.lista_trabajadores'),
    url(r'^agregar/$','principal.views.nuevo_trabajador'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^eliminar/$','principal.views.eliminar_usuario'),
    url(r'^agregado/$','principal.views.agregado'),
    
)
