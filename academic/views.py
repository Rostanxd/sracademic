# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def menu (request):
    return render(request, 'security/menu.html',)


def nivel (request):
    return render(request, 'security/nivel.html',)


def materias (request):
    return render(request, 'security/materias.html',)


def profesores (request):
    return render(request, 'security/profesores.html',)