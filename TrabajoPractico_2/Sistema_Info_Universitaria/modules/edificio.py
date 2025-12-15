from modules.persona import Estudiante, Profesor


class Facultad():
    """Esta clase contiene todos los metodos para estudiante, profesor, cursos y departamento"""

    def __init__(self, nombre_facultad):
        self.__nombre_facultad = nombre_facultad
        self.__lista_estudiantes = []
        self.__lista_profesores = []
        self.__lista_departamentos = []

    def inscripcion_estudiante(self, estudiante):
        """Este metodo regritra los datos del estudiante que sera inscripto"""

        if isinstance (estudiante, Estudiante):
            self.__lista_estudiantes.append(estudiante)

    def mostrar_lista_estudiantes(self):
        """Este metodo muestra la lista de estudiantes inscriptos"""

        salida = "\nLista de estudiantes\n"
        for indice, estudiante in enumerate(self.__lista_estudiantes, 1):
            salida += str(indice) + ". " + estudiante.nombre + " " + estudiante.apellido + " " + str(estudiante.dni) + "\n"
        
        return salida
    
    def mostrar_lista_profesores (self):
        """Este metodo muestra la lista de profesores"""

        salida = "\nLista de profesores\n"
        for indice, profesor in enumerate(self.__lista_profesores, 1):
            salida += str(indice) + ". " + profesor.nombre + " " + profesor.apellido + " " + str(profesor.dni) + "\n"

        return salida
    
    def mostrar_lista_departamentos (self):
        """Este metodo muestra la lista de departamentos"""

        salida = "\nLista de departamentos\n"

        for indice, departamentos in enumerate(self.__lista_departamentos, 1):
            salida += str(indice) + ". " + departamentos.nombre_departamento + ", director: " + departamentos.director.nombre + " " + departamentos.director.apellido + "\n"

        return salida
    
    def mostrar_cursos_del_departamento (self, id_departamento):
        """Este metodo muestra una lista de los cursos de un determiando departamento"""

        departamento = self.__lista_departamentos[id_departamento - 1]
        cursos = departamento.mostrar_lista_cursos()

        return cursos
    
    def inscribir_profesor(self, profesor):
        """Este metodo agrega el profesor contratado"""

        if isinstance (profesor,Profesor):
            self.__lista_profesores.append(profesor)

    def verificar_si_el_profesor_es_director(self,director_elegido):
        """Este metodo determina si el profesor es el director de un departamento"""
        for departamento in self.__lista_departamentos:
            if departamento.director == director_elegido:
                return True
        return False
    
    def verificacion_titularidad_del_curso (self, profesor):
        """Este metodo verifica si un profesor ya es titular de un curso"""
        for departamento in self.__lista_departamentos:
            for curso in departamento.mostrar_lista_de_cursos_creada():
                if curso.titular_del_curso == profesor:
                    return True      
        return False
    
    """def mostrar_lista_profesores_para_ser_director (self):
        Este metodo muestra la lista de los profesores que podrian ser directores de un departamento

        salida = "\nLista de profesores disponibles:\n"
        for indice, profesor in enumerate(self.__lista_profesores, 1):
                if not self.determinar_director(indice):
                    salida += str(indice) + ". Nombre: " + profesor.nombre + " " + profesor.apellido + ", dni: " + str(profesor.dni) + "\n"
        return salida"""
        
    
    """def mostrar_lista_profesores_para_ser_titular(self):
        Este metodo muestra la lista de los profesores que podrian ser titulares de un curso

        salida = "\nLista de profesores disponibles para ser titulares\n"
        for indice, profesor in enumerate(self.__lista_profesores, 1):
            salida += str(indice) + ". " + profesor.nombre + " " + profesor.apellido + " " + str(profesor.dni) + "\n"

        return salida"""
    
    def crear_departamento (self, departamento, id_director):
        """Este metodo crea un departamento nuevo"""
        
        director_elegido = self.__lista_profesores [id_director - 1]
        if self.verificar_si_el_profesor_es_director (director_elegido) == False:
            self.__lista_departamentos.append (Departamento(departamento, director_elegido))
        else: 
            print ("Este profesor ya es titular de un curso")

    def crear_curso(self, id_departamento, nombre_curso, id_titular):
        """Este metodo para crear un nuevo curso"""

        departamento_elegido = self.__lista_departamentos [id_departamento - 1]
        titular_elegido= self.__lista_profesores [id_titular-  1]
        if self.verificacion_titularidad_del_curso(titular_elegido) == True:
            raise ValueError ("Este profesor ya es titular de un curso en otro departamento.")
        else:
            departamento_elegido.crear_nuevo_curso(nombre_curso, titular_elegido)

    def asignacion_curso_a_estudiante(self, id_departamento, id_curso, id_estudiante):
        """ Este metodo asigna un curso a un estudiante"""
        
        curso = self.__lista_departamentos[id_departamento - 1].devuelve_curso(id_curso)
        estudiante_seleccionado = self.__lista_estudiantes[id_estudiante - 1]
        self.__lista_departamentos[id_departamento - 1].asigno_estudiante_a_curso(id_estudiante, id_curso)
        self.__lista_estudiantes[id_estudiante - 1].inscripcion_a_curso(curso)
        print("El estudiante " + estudiante_seleccionado.nombre + " " + estudiante_seleccionado.apellido + " es asignado al curso " + curso.nombre_curso + ".")

class Departamento():
    """ Esta clase contiene los metodos departamentos y curso"""

    def __init__(self, departamento, director):
        self.__nombre_departamento = departamento
        self.__director = director 
        self.__lista_cursos = []
  
    @property
    def nombre_departamento(self):
        return self.__nombre_departamento

    @property
    def director(self):
        return self.__director
    
    def crear_nuevo_curso (self, curso, titular):

        if isinstance (titular, Profesor):
            curso_nuevo = Curso(curso, titular)
            self.__lista_cursos.append(curso_nuevo)
            titular.curso_titular = curso_nuevo

    def mostrar_lista_cursos(self):
        """Este metodo muestra una lista de cursos"""

        salida = "\nLista de cursos:\n"
        for indice, curso in enumerate(self.__lista_cursos, 1):
            salida += str(indice) + ". " + curso.nombre_curso + ", titular: " +  curso.titular_del_curso.nombre + " "+  curso.titular_del_curso.apellido + "\n"
        return salida
    
    def mostrar_lista_de_cursos_creada(self):
        """Este metodo muestra la lista de cursos creados"""
        return self.__lista_cursos
    
    def asigno_estudiante_a_curso(self, estudiante, curso):
        self.__lista_cursos[curso-1].asignar_estudiante(estudiante)

    def devuelve_curso (self, indice_curso):
        return self.__lista_cursos[indice_curso-1]
        
    
class Curso():
    """Esta clase contiene el metodo para asignar un estudiante a un curso"""

    def __init__(self, nombre_curso, titular):
        self.__nombre_curso = nombre_curso
        self.__titular_del_curso = titular
        self.__lista_alumnos_de_un_curso = []

    @property
    def nombre_curso(self):
        return self.__nombre_curso
    
    @property
    def titular_del_curso(self):
        return self.__titular_del_curso   
     
    def asignar_estudiante(self, estudiante):
        if isinstance (estudiante, Estudiante):
            if estudiante not in self.__lista_alumnos_de_un_curso:
                self.__lista_alumnos_de_un_curso.append(estudiante)
                estudiante.inscripcion_a_curso(self.__nombre_curso)

