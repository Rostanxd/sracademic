# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import NivelAcademico, Materia, Distributivo

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

import json


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


#   Función de logueo
def login_view(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')

    user = authenticate(username=username, password=password)

    login = False
    error = 1
    err_msg = 'Incorrect username or password.'
    if user is not None:
        login = True
        error = 0
        err_msg = ''

    data = {
        'error': error,
        'err_msg': err_msg,
        "login": login
    }

    return HttpResponse(json.dumps(data), content_type="application/json")


#   Función de salir
def logout_view(request):
    logout(request)
    data = {
        'error': 0,
        'err_msg': '',
        'logout': True
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


#   Pagineo o redireccionamiento de las páginas
def menu(request):
    return render(request, '../templates/security/menu.html', )


def niveles_academicos(request):
    niveles = NivelAcademico.objects.all()
    niveles_arr = []
    for n in niveles:
        niveles_arr.append({
            'pk': n.pk,
            'nombre': n.nombre,
            'fecha_inicio': n.fechainicio,
            'fecha_fin': n.fechafin,
            'fecha_matricula': n.fechamatriculaordinaria,
            'fecha_especial': n.fechamatriculaespecial,
            'fecha_extraordinaria': n.fechamatriculaextraordinaria,
            'id_sesion': n.sesion.id,
            'sesion': n.sesion.nombre,
            'matriculas': n.matriculas,
            'modalidad': n.modalidad.nombre,
        })
    return render(request, 'security/niveles_academicos.html', context={'niveles': niveles_arr})


def nivel_academico_detalle(request, pk):
    nivel_academico = get_object_or_404(NivelAcademico, pk=pk)
    distributivos = Distributivo.objects.filter(sesion__exact=nivel_academico.sesion.id)
    distributivos_arr = []
    for d in distributivos:
        distributivos_arr.append({
            'pk': d.pk,
            'materia': d.materia.nombre
        })

    return render(request,
                  'security/nivel_academico_detalle.html',
                  context={
                      'nivel_academico': nivel_academico,
                      'distributivos': distributivos_arr
                  })


def distributivo_detalle(request, pk):
    try:
        distributivo = get_object_or_404(Distributivo, pk=pk)
        return render(request, 'security/distributivo_detalle.html', context={'distributivo': distributivo})
    except Materia.DoesNotExist:
        raise Http404("No MyModel matches the given query.")


def profesor(request):
    return render(request, 'security/distributivo_detalle.html', )


#   Funciones de consultas
def get_niveles(request):
    niveles = NivelAcademico.objects.all()
    niveles_arr = []
    for n in niveles:
        niveles_arr.append({
            'nombre': n.nombre,
            'fecha_inicio': n.fechainicio,
            'fecha_fin': n.fechafin,
            'fecha_matricula': n.fechamatriculaordinaria,
            'sesion': n.sesion.nombre,
            'matriculas': n.matriculas
        })

    return HttpResponse(JSONResponse(niveles_arr), content_type="application/json")
