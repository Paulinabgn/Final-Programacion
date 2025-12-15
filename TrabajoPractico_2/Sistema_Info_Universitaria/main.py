from modules.funciones_obtener import obtengo_lista_estudiantes, obtengo_lista_profesores
from modules.persona import Estudiante, Profesor
from modules.edificio import  Facultad

facultad = Facultad("Facultad de Bioingenieria")

RUTA = "data/"
archivo_estudiantes = RUTA + "estudiantes.txt"
lista_informacion_de_estudiantes = obtengo_lista_estudiantes(archivo_estudiantes)
lista_estudiantes=[]
for datos_estudiante in lista_informacion_de_estudiantes:
    estudiante = Estudiante(datos_estudiante[0], datos_estudiante[1], datos_estudiante[2])
    facultad.inscripcion_estudiante(estudiante)
    lista_estudiantes.append(estudiante)

RUTA = "data/"
archivo_profesor = RUTA + "profesores.txt"
informacion_profesor = obtengo_lista_profesores(archivo_profesor)
lista_profesores = []
for profesor in informacion_profesor:
    profesor=Profesor(profesor[0], profesor[1], profesor[2])
    facultad.inscribir_profesor(profesor)
    lista_profesores.append(profesor)

facultad.crear_departamento("Matematica", 1)
facultad.crear_curso(1, "Funciones de variable compleja", 1)

menu= """
Sistema de informacion universitaria 

Elige una opcion
1 - Inscribir alumno
2 - Contratar profesor
3 - Crear departamento nuevo
4 - Crear curso nuevo
5 - Inscribir estudiante a un curso
6 - Salir
"""

opcion = 0
while opcion != 6:
    print(menu)
    opcion = int(input("Ingrese una opcion: ")) 
    if opcion == 1:
        nombre_alumno = input("Ingrese el nombre del alumno: ")
        apellido_alumno = input("Ingrese el apellido del alumno: ")
        dni_alumno = int(input("Ingrese el dni del alumno: "))
        estudiante = Estudiante(nombre_alumno, apellido_alumno, dni_alumno)
        lista_estudiantes.append(estudiante)
        facultad.inscripcion_estudiante(estudiante)

    elif opcion == 2:
        nombre_profesor = input("Ingrese el nombre del profesor: ")
        apellido_profesor = input("Ingrese el apellido del profesor: ")
        dni_profesor = input("Ingrese el dni del profesor: ")
        profesor = Profesor(nombre_profesor, apellido_profesor, dni_profesor)
        lista_profesores.append(profesor)
        facultad.inscribir_profesor(profesor)

    elif opcion == 3: 
        nuevo_departamento = input("Ingrese el nombre del nuevo departamento: ")
        print(facultad.mostrar_lista_profesores())
        nuevo_director = int(input("Elija cual sera el director: "))
        facultad.crear_departamento(nuevo_departamento, nuevo_director)
        print(facultad.mostrar_lista_departamentos())

    elif opcion == 4:
        nuevo_curso = input("Ingrese el nombre del nuevo curso: ")
        print(facultad.mostrar_lista_profesores())
        nuevo_titular = int(input("Elija el titular del curso: "))
        print(facultad.mostrar_lista_departamentos())
        asignar_departamento = int(input("Elija el departamento del cual sera parte el curso: "))
        facultad.crear_curso(asignar_departamento, nuevo_curso, nuevo_titular)
        print(facultad.mostrar_cursos_del_departamento(asignar_departamento))

    elif opcion == 5:
        print(facultad.mostrar_lista_departamentos())
        departamento_elegido = int(input("Ingrese departamento: "))
        print(facultad.mostrar_cursos_del_departamento(departamento_elegido))
        incribir_estudiante_curso = int(input("Elija el curso: "))
        print(facultad.mostrar_lista_estudiantes())
        asigne_estudiante_curso=int(input("Elija el estudiante que asignara al curso: "))
        facultad.asignacion_curso_a_estudiante(departamento_elegido, incribir_estudiante_curso, asigne_estudiante_curso)
       