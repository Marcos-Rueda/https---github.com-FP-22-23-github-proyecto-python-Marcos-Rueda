from collections import namedtuple
from datetime import datetime
import csv

Pacientes=namedtuple("Pacientes","cod_paciente,colesterol,trigliceridos,hemoglobina,sexo,fecha")

def lee_fichero_pacientes(nombre_fich):
    print("\tLectura de pacientes: ")
    lista=[]
    with open(nombre_fich) as f:
        lector=csv.reader(f, delimiter=",")
        next(lector)
        for cod_paciente, colesterol, trigliceridos, hemoglobina, sexo, fecha in lector:
            hemoglobina=float(hemoglobina)
            trigliceridos=int(trigliceridos)
            fecha1=fecha(fecha.strip())
            tupla=Pacientes(cod_paciente,colesterol,trigliceridos,hemoglobina,sexo,fecha1)
            lista.append(tupla)
    return lista

def parse_fecha(cadena):
    fecha=datetime.strptime(cadena, '%d/%m/%Y').date()
    return fecha

def condicion_sexo(lista, sexo):
    res=[ t for t in lista if t.sexo==sexo]
    return res

def promedio_trigliceridos(lista, sexo):
    lista_auxiliar=[tupla.trigliceridos for tupla in lista if tupla.sexo==sexo]
    suma=sum(lista_auxiliar)
    total_elem=len(lista_auxiliar)
    return suma/total_elem

def pacientes_mayor_colesterol(lista, sexo, n=10):
    lista_auxiliar=[tupla for tupla in lista if tupla.sexo==sexo]
    lista_auxiliar.sort(key=lambda x:x.colesterol, reverse=True)
    lista_codpaciente=[tupla.cod_paciente for tupla in lista_auxiliar]
    res=[]
    for cod_paciente in lista_codpaciente:
        if cod_paciente not in res:
            res.append(cod_paciente)
    return res[:n]

def mujer_mayor_colesterol(lista, sexo):
    lista_aux=[tupla for tupla in lista if tupla.sexo==sexo]
    tupla_max=max(lista_aux, key=lambda x:x.colesterol)
    return tupla_max.colesterol

def mujer_mayor_colesterol_y_hemoglobina(lista, sexo):
    lista_aux=[tupla for tupla in lista if tupla.sexo==sexo and tupla.hemoglobina<=6.0]
    tupla_max=max(lista_aux, key=lambda x:x.colesterol)
    return tupla_max.colesterol