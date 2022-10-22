from collections import namedtuple
from datetime import datetime
import csv

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
            fecha1=parse_fecha(fecha.strip())
            tupla=Pacientes(cod_paciente,colesterol,trigliceridos,hemoglobina,sexo,fecha1)
            lista.append(tupla)
    return lista

def parse_fecha(cadena):
    fecha=datetime.strptime(cadena, '%d/%m/%Y').date()
    return fecha

if __name__=="__main__":
    res=lee_fichero_pacientes('./data/estudio_pacientes.csv')
    print(res)
