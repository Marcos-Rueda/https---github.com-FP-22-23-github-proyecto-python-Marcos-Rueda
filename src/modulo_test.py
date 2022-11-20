from collections import namedtuple
from datetime import datetime
import csv
from funciones_principales import *

# cod_paciente, colesterol, trigliceridos, hemoglobina, sexo, fecha
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
            fecha1=parse_fecha(fecha.strip())
            tupla=Pacientes(cod_paciente,colesterol,trigliceridos,hemoglobina,sexo,fecha1)
            lista.append(tupla)
    return lista

def parse_fecha(cadena):
    fecha=datetime.strptime(cadena, '%d/%m/%Y').date()
    return fecha

def test_condicion_sexo(lista):
    print("------------Obtener una lista de tuplas igual que la original pero solo con aquellos registros que verifican una condición: ")
    lista_h=condicion_sexo(lista, ' mujer')
    print("Lista de mujeres:")
    print(lista_h)

def test_promedio_trigliceridos(lista):
    print("------------Una función que devuelva la suma, promedio o un cálculo sobre las tuplas o parte de ellas: ")
    sexo=" hombre"
    media=promedio_trigliceridos(lista, sexo)
    print(f'La media de trigliceridos en {sexo} es de {media}')

def test_pacientes_mayor_colesterol(lista):
    print("-----------Función que obtenga una lista con n registros ordenados de mayor a menor por un campo determinado de entre los que cumplan una condición: ")
    n=5
    sexo=" hombre"
    col=pacientes_mayor_colesterol(lista, sexo, n)
    print(f"Hombres con el registro de mayor colesterol: {col}")

def test_mujer_mayor_colesterol(lista):
    print("------------Función que obtenga un máximo o un mínimo respecto a algún campo determinado: ")
    sexo=" mujer"
    coles=mujer_mayor_colesterol(lista, sexo)
    print(f"El mayor número de colesterol registrado en una mujer es de: {coles}")

def test_mujer_mayor_colesterol_y_hemoglobina(lista):
    sexo=" mujer"
    print("------------Función adicional: ")
    lista_mayor=mujer_mayor_colesterol_y_hemoglobina(lista, sexo)
    print(f"La mujer con más colesterol con una hemoglobina menor de 6.0 es de: {lista_mayor}")

if __name__=="__main__":
    res=lee_fichero_pacientes('./data/estudio_pacientes.csv')
    print(res)
    test_condicion_sexo(res)
    test_promedio_trigliceridos(res)
    test_pacientes_mayor_colesterol(res)
    test_mujer_mayor_colesterol(res)
    test_mujer_mayor_colesterol_y_hemoglobina(res)

