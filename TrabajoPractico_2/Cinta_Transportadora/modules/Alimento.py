from abc import ABC, abstractmethod
import math

class Alimento(ABC):
    """Clase abstracta que representa un alimento del cajon"""
    
    def __init__ (self, masa):
        if masa < 0:
            raise ValueError("La masa no puede ser negativa.")
        if masa > 0.6:
            raise ValueError("La masa no puede ser mayor a 600 gramos.")
        self.__masa = masa

    @property
    def masa (self):
        return self.__masa

    @abstractmethod
    def calcular_aw (self):
        pass

class Fruta (Alimento):
    """Clase que representa una Fruta"""

    def __init__ (self, masa):
        super().__init__ (masa)

class Verdura (Alimento):
    """Clase que representa una Verdura"""

    def __init__ (self, masa):
        super().__init__ (masa)

class Kiwi (Fruta):
    """Clase que representa un Kiwi"""

    def __init__ (self, masa):
        super().__init__ (masa)
    
    def calcular_aw (self):
        C = 18
        Cm = C * self.masa
        aw_kiwi = 0.96 * ((1 - math.exp (-Cm)) / (1 + math.exp (-Cm)))
        return round (aw_kiwi, 2)

class Manzana (Fruta):
    """Clase que representa una Manzana"""

    def __init__ (self, masa):
        super().__init__ (masa)
    
    def calcular_aw (self):
        C = 15
        Cm = C * self.masa
        aw_manzana = 0.97 * (((Cm)**2) / (1 + ((Cm)**2)))
        return round (aw_manzana, 2)

class Papa (Verdura):
    """Clase que representa una Papa"""

    def __init__ (self, masa):
        super().__init__ (masa)
    
    def calcular_aw (self):
        C = 18
        Cm = 18 * self.masa
        aw_papa = 0.66 * (math.atan(Cm))
        return round (aw_papa, 2)

class Zanahoria (Verdura):
    """Clase que representa una Zanahoria"""

    def __init__ (self, masa):
        super().__init__ (masa)
    
    def calcular_aw (self):
        C = 10
        Cm = C * self.masa
        aw_zanahoria = 0.96 * (1 - math.exp(-Cm))
        return round (aw_zanahoria, 2)