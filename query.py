import os
import django
import openpyxl
from openpyxl.worksheet import worksheet
import sys
reload(sys)
sys.setdefaultencoding('utf8')

os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sracademic.settings")
django.setup()
from django.contrib.auth.models import User
from django.db import transaction
from sracademic.settings import BASE_DIR
from academic.models import *
from datetime import date


def del_espace(element):
    element = element.strip()
    newelement = ''
    lenght = len(element) - 1
    count = 0
    while count <= lenght:
        if element[count] == ' ':
            if element[count + 1] != ' ':
                newelement += element[count]
        else:
            newelement += element[count]
        count += 1
    return newelement

currentValues = []
line = 1
currentValues = []
fechaIngreso = date(2019, 6, 18)
try:
    archivo = BASE_DIR + '\\Semestres.xlsx'
    wb = openpyxl.load_workbook(archivo)
    worksheet = wb["Hoja1"]
    with transaction.atomic():
        for row in worksheet.iter_rows(min_row=1):
            currentValues = []
            counter = 0
            for cell in row:
                currentValues.append(str(cell.value))
            materias =Materia(nombre=currentValues[0],fechainicio=fechaIngreso, fechafin=fechaIngreso,cupo=0,credito=currentValues[1],horassemanal=0)
            materias.save()
            print(str(currentValues))

            counter += 1
            line += 1
except Exception as ex:
    print(ex)
    print(str(line))
    print(currentValues)



