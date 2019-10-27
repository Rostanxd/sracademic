from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'academic'

urlpatterns = [
    url(r'^menu', views.menu, name='menu'),
    url(r'^niveles_academicos', views.niveles_academicos, name='niveles_academicos'),
    url(r'^nivel_academico_detalle/(?P<pk>[0-9a-zA-Z]+)',
        views.nivel_academico_detalle,
        name='nivel-academico-detalle'),
    url(r'^distributivo_detalle/(?P<pk>[0-9a-zA-Z]+)',
        views.distributivo_detalle,
        name='distributivo-detalle'),
    url(r'^profesor', views.profesor, name='profesor'),
    url(r'^get_nivel', views.get_niveles, name='get_niveles'),
]
