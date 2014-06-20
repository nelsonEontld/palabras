from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^prueba/$', 'aplicaciones.palabrasFrases.views.vistaDePrueba'),    
    url(r'^beto/$', 'aplicaciones.palabrasFrases.views.vistaDePrueba'),    
    url(r'^busqueda_ajax/', 'aplicaciones.palabrasFrases.views.busquedaAjaxView'),
)
