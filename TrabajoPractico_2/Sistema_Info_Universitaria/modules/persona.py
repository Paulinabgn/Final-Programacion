from abc import ABC, abstractmethod

class Persona (ABC):
    """Esta clase abstracta representa UNA persona"""

    def __init__ (self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    
    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nombre):
        self.__nombre = nombre


    @property
    def apellido (self):
        return self.__apellido
    
    @nombre.setter
    def nombre (self, apellido):
        self.__apellido = apellido

    
    @property
    def dni (self):
        return self.__dni
    
    @nombre.setter
    def nombre (self, dni):
        self.__dni = dni


class Estudiante(Persona):
    """Esta clase representa un estudiante que es una persona"""

    def __init__(self, nombre_estud, apellido_estud, dni_estud):
        super().__init__(nombre_estud, apellido_estud, dni_estud)
        self.__cursos_del_estudiante = []

    def inscripcion_a_curso (self, curso):
        self.__cursos_del_estudiante.append(curso)


class Profesor(Persona):
    """Esta clase representa un profesor que es una persona"""

    def __init__ (self, nombre_profe, apellido_profe, dni_profe):
        super().__init__(nombre_profe, apellido_profe, dni_profe)
        self.__director = False
        self.__curso_titular = None

    @property
    def curso_titular(self):
        return self.__curso_titular
    
    @curso_titular.setter
    def curso_titular(self, curso_titular):
        self.__curso_titular = curso_titular

    @property
    def director (self):
        return self.__director

    @director.setter
    def director (self, director):
        self.__director = director

if __name__ == "__main__":
    estudiante_1 = Estudiante("Marcelo", "Zanguelini", 90123456)
    profesor_1 = Profesor("Celina", "Bratovich", 10234567)

