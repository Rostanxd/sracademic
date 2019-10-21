# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


class Semestre(models.Model):
    nombre = models.CharField(max_length=200)
    alias=models.CharField(max_length=200)

    def __str__(self):
        return "{}{}".format(self.nombre,self.alias)

    class Meta:
        verbose_name = 'Semestre'
        verbose_name_plural = "Semestres"
        ordering = ('nombre',)


class Carrera(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = "Carreras"
        ordering = ('nombre',)


class Paralelo(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Paralelo'
        verbose_name_plural = "Paralelos"
        ordering = ('nombre',)


class Sesion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Sesion'
        verbose_name_plural = "Sesiones"
        ordering = ('nombre',)


class SubAreaConocimientoEspecifico(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Sub Area de Conocimiento Especifico'
        verbose_name_plural = "Area de Conocimiento Especifico"
        ordering = ('nombre',)


class SubAreaConocimiento(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Sub Area de Conocimiento'
        verbose_name_plural = "Sub Area de Conocimiento"
        ordering = ('nombre',)


class AreaConocimiento(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Area de Conocimiento'
        verbose_name_plural = "Area de Conocimientos"
        ordering = ('nombre',)

class Grado(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = "Grados"
        ordering = ('nombre',)


class TipoNivel(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Tipo Nivel'
        verbose_name_plural = "Tipos de Niveles"
        ordering = ('nombre',)


class PeriodoAcademico(models.Model):
    descripcion = models.CharField(max_length=200)
    fechaInicio = models.DateField(verbose_name='Fecha de Inicio')
    fechaFin = models.DateField(verbose_name='Fecha de Fin')

    def __str__(self):
        return "{}: {} a {}".format(self.descripcion, self.fechaInicio, self.fechaFin)

    class Meta:
        verbose_name = 'Periodo Academico'
        verbose_name_plural = "Periodos Academicos"
        ordering = ('fechaInicio', 'fechaFin',)


class Facultad(models.Model):
    nombre = models.CharField(max_length=200)
    alias = models.CharField(max_length=200,default='')

    def __str__(self):
        return "{}{}".format(self.nombre,self.alias)

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = "Facultades"
        ordering = ('nombre',)

class Persona(models.Model):
    nombres = models.CharField(max_length=200, default='')
    apellidos = models.CharField(max_length=200, default='')
    documento = models.CharField(max_length=20, default='')
    correo = models.CharField(max_length=200, default='')
    fechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento', default=timezone.now)
    celular = models.CharField(max_length=20, default='')
    telefono = models.CharField(max_length=20, default='')
    direccion = models.CharField(max_length=200, default='')

    def __str__(self):
        return "{} {} | {}".format(self.apellidos, self.nombres, self.documento)

    def datos(self):
        return "{} {}".format(self.apellidos, self.nombres)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = "Personas"
        ordering = ('nombres',)

class Docente(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to='local/%Y/%m', null=True, blank=True, verbose_name='foto')

    def __str__(self):
        return "{}".format(self.persona.datos())

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = "Profesores"
        ordering = ('persona',)


class Estudiante(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)

    def __str__(self):
        return "{}".format(self.persona.datos())

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = "Estudiantes"
        ordering = ('persona',)


class Modalidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = "Modalidades"
        ordering = ('nombre',)


class NivelAcademico(models.Model):
    nombre = models.CharField(max_length=200, default='')
    modalidad = models.ForeignKey(Modalidad, on_delete=models.PROTECT)
    sesion = models.ForeignKey(Sesion, on_delete=models.PROTECT)
    fechainicio = models.DateField(verbose_name='Fecha inicio', default=timezone.now)
    fechafin = models.DateField(verbose_name='Fecha fin', default=timezone.now)
    fechamatriculaordinaria= models.DateField(verbose_name='Fecha matricula ordinaria', default=timezone.now)
    fechamatriculaextraordinaria = models.DateField(verbose_name='Fecha matricula ordinaria', default=timezone.now)
    fechamatriculaespecial = models.DateField(verbose_name='Fecha matricula especial', default=timezone.now)

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.nombre, self.modalidad.nombre, self.sesion.nombre,self.fechafin,self.fechafin,
                                       self.fechamatriculaordinaria,self.fechamatriculaextraordinaria,self.fechamatriculaespecial)

    class Meta:
        verbose_name = 'Nivel Academico'
        verbose_name_plural = "Nivel Academico"
        ordering = ('nombre',)


class Investigacion(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=200)
    areaconocimiento = models.ForeignKey(AreaConocimiento, on_delete=models.PROTECT)
    subareaconocimiento = models.ForeignKey(SubAreaConocimiento, on_delete=models.PROTECT)
    areaconocimientoespecifico = models.ForeignKey(SubAreaConocimientoEspecifico, on_delete=models.PROTECT)
    def __str__(self):
        return "{}".format(self.docente.persona.datos())

    class Meta:
        verbose_name = 'Investigacion'
        verbose_name_plural = "Investigaciones"
        ordering = ('docente',)


class Titulacion(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=200)
    tiponivel =models.ForeignKey(TipoNivel, on_delete=models.PROTECT)
    grado =models.ForeignKey(Grado, on_delete=models.PROTECT)
    areaconocimiento = models.ForeignKey(AreaConocimiento, on_delete=models.PROTECT)
    subareaconocimiento = models.ForeignKey(SubAreaConocimiento, on_delete=models.PROTECT)
    areaconocimientoespecifico = models.ForeignKey(SubAreaConocimientoEspecifico, on_delete=models.PROTECT)
    def __str__(self):
        return "{}".format(self.docente.persona.datos())

    class Meta:
        verbose_name = 'Investigacion'
        verbose_name_plural = "Investigaciones"
        ordering = ('docente',)

class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    fechainicio = models.DateField(verbose_name='Fecha inicio', default=timezone.now)
    fechafin = models.DateField(verbose_name='Fecha fin', default=timezone.now)
    cupo = models.IntegerField( default=0)
    credito= models.DecimalField(default=0, max_digits=16, decimal_places=4)
    horassemanal = models.IntegerField(default=0)
    def __str__(self):
        return " {} {} {} {} {} {}".format(self.nombre,self.fechainicio,self.fechafin,self.cupo,self.credito,self.horassemanal)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = "Materias"
        ordering = ('nombre',)


class Evaluacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    puntuacion = models.DecimalField(default=0, max_digits=16, decimal_places=2)

    def __str__(self):
        return "{}".format(self.putuacion)

    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = "Evaluaciones"
        ordering = ('estudiante',)


class Distributivo(models.Model):
    peridoacademico = models.ForeignKey(PeriodoAcademico, on_delete=models.PROTECT)
    facultad = models.ForeignKey(Facultad, on_delete=models.PROTECT)
    carera = models.ForeignKey(Carrera, on_delete=models.PROTECT)
    semestre = models.ForeignKey(Semestre, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    paralelo = models.ForeignKey(Paralelo, on_delete=models.PROTECT)
    docente = models.ForeignKey(Docente, on_delete = models.PROTECT)

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.peridoacademico.descripcion,self.facultad.nombre,self.carera.nombre,self.semestre.nombre,
                           self.materia.nombre,self.paralelo.nombre,self.docente.persona.nombres)

    class Meta:
        verbose_name = 'Distributivo'
        verbose_name_plural = "Distributivo"
        ordering = ('peridoacademico',)

