from modules.Alimento import Alimento

class Cajon:

    def __init__ (self):
        self.__alimento_recibido = []

    def agregar_alimento (self, alimento):
        if isinstance (alimento, Alimento):
            self.__alimento_recibido.append (alimento)

    def devolver_cantidad_de_alimentos (self):
        return len (self.__alimento_recibido)

    def __iter__ (self):
        """Método especial que permite iterar sobre los alimentos en el cajón
        """
        return iter (self.__alimento_recibido)