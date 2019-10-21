from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'academic'

urlpatterns = [
    url(r'^menu', views.menu, name='menu'),
    url(r'^distributivo', views.distributivo, name='distributivo'),
    url(r'^materia/(?P<pk>[0-9a-zA-Z]+)', views.materia, name='materia'),
    url(r'^profesor', views.profesor, name='profesor'),
    url(r'^get_nivel', views.get_niveles, name='get_niveles'),
]
