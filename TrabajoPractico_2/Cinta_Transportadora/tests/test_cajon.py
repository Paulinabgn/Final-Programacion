import unittest
from modules.Cajon import Cajon
from modules.Alimento import Alimento

class AlimentoConcreto(Alimento):
    def calcular_aw(self):
        return 0.0  # Implementación ficticia para la prueba

class TestCajon (unittest.TestCase):
    def setUp (self):
        self.cajon = Cajon ()
    
    def test_agregar_alimento_y_devolver_cantidad (self):
        # Crea un alimento válido usando la subclase concreta
        alimento_valido = AlimentoConcreto (0.5)
        # Agrega el alimento al cajon
        self.cajon.agregar_alimento (alimento_valido)
        # Verifica que el conteo del cajon sea 1
        self.assertEqual (self.cajon.devolver_cantidad_de_alimentos(), 1)
        
        # Crea otro alimento válido
        alimento_valido_2 = AlimentoConcreto (0.2)
        # Agrega este segundo alimento al cajón
        self.cajon.agregar_alimento (alimento_valido_2)
        # Verifica que el conteo sea 2
        self.assertEqual (self.cajon.devolver_cantidad_de_alimentos(), 2)

        # Intenta agregar un alimento no válido
        self.cajon.agregar_alimento ("Pera")
        # Verifica que la cuenta de alimentos no se haya incrementado
        self.assertEqual (self.cajon.devolver_cantidad_de_alimentos(), 2)
