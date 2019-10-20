from django.conf.urls import url
from django.contrib import admin
from .views import menu, nivel, materias, profesores

urlpatterns = [
    url(r'^menu/', menu, name='menu'),
    url(r'^nivel/', nivel, name='nivel'),    
    url(r'^materias/', materias, name='materias'),
    url(r'^profesores/', profesores, name='profesores')
]
