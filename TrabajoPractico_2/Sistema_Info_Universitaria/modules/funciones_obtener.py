

def obtengo_lista_estudiantes (archivo):
    informacion_de_estudiantes = []
    with open(archivo,"r") as archi:
        for dato in archi:
            nombre, apellido, dni = dato.rstrip().split(" ")
            nombre = str(nombre)
            apellido = str(apellido)
            dni = int(dni)
            informacion_de_estudiantes.append([nombre, apellido, dni])
    return informacion_de_estudiantes

def obtengo_lista_profesores(archivo):
    lista_profesores = []
    with open (archivo,"r") as archi:
        for i in archi:
            nombre, apellido, dni =  i.split(" ")
            nombre = str(nombre)
            apellido = str(apellido)
            dni = int(dni)
            lista_profesores.append([nombre, apellido, dni])
    return lista_profesores
