Para este proyecto se ha utilizado una función de lectura de fichero csv, utilizando la función namedtuple, esta función nos devuelve una lista de tuplas con el contenido del fichero csv, en este caso, estudio_pacientes.csv

Función empleada:
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

Funciones implementadas:
    1-Una función que te devuelve una lista de tuplas igual que la original pero pero solo con aquellos registros que verifican una condición. En este caso he puesto que devuelva una lista de tuplas registrado por mujeres.
    2-Una función que devuelva la suma, promedio o un cálculo sobre las tuplas o parte de ellas. En esta función he puesto que nos devueva la media de trigliceridos en los hombres.
    3-Función que obtenga una lista con n registros ordenados de mayor a menor por un campo determinado de entre los que cumplan una condición. Para esta, la función nos devuelve una lista con los 5 pacientes que más colesterol hay registrados.
    4-Función que obtenga un máximo o un mínimo respecto a algún campo determinado. En este caso la función nos devuelve el máximo de colesterol registrado en una mujer.
    5-Cualquier función del tipo de las funciones adicionales que explicaremos con el proyecto Nombres. En esta última, la función nos devuelve el colesterol más alto en una mujer si la mujer tiene una hemoglobina por debajo de 6.0.